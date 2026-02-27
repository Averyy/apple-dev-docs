# Implementing a virtual conference extension

**Framework**: EventKit

Support adding a virtual conference room to an event in Calendar.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- Xcode 26.2+

#### Overview

This sample code project demonstrates how to implement a virtual conference extension using [`EKVirtualConferenceProvider`](ekvirtualconferenceprovider.md). With this extension, people can add a virtual conference room to an event in Calendar, by selecting the room from a list in the event’s Location field. The sample code extension uses a single target that supports iOS and macOS.

##### Configure the Sample Code Project

To configure the sample code project, do the following in Xcode:

1. Open the sample in the latest version of Xcode.
2. For all targets in the sample project, choose your team from the Team menu in the Signing & Capabilities pane to let Xcode automatically manage your provisioning profile. For more information, see “Set the bundle ID” and “Assign the project to a team” in [`Preparing your app for distribution`](https://developer.apple.com/documentation/Xcode/preparing-your-app-for-distribution).

##### Add a Virtual Conference Extension Target to Your Project

To create a virtual conference extension, add a virtual conference extension target to your new or existing Xcode project.

To add a virtual conference extension target, follow these steps:

1. Choose File > New > Target.
2. In the sheet that appears, choose the platform your app supports. For instance, select the Virtual Conference template under the iOS platform. If your app supports an additional platform such as macOS, add the platform as a destination to the created extension. For more information, see “Configure the supported destinations for a target” in  [`Configuring a multiplatform app`](https://developer.apple.com/documentation/Xcode/configuring-a-multiplatform-app-target).
3. Scroll down to the Application Extension section.
4. Select the Virtual Conference template.
5. Click Next.
6. Specify the name of your extension and leave the other values set to their defaults.
7. Click Finish.

##### Review the Generated Virtual Conference Extension Files

The Virtual Conference template creates an `Info.plist` file and the `VirtualConferenceProvider` class. The `Info.plist` file includes an `NSExtensionPointIdentifier` key and an `NSExtensionPrincipalClass` key under the `NSExtension` key:

```None
<plist>
    <dict>
        <key>NSExtension</key>
        <dict>
            <key>NSExtensionPointIdentifier</key>
            <string>com.apple.calendar.virtualconference</string>
            <key>NSExtensionPrincipalClass</key>
            <string>$(PRODUCT_MODULE_NAME).VirtualConferenceProvider</string>
        </dict>
    </dict>
</plist>
```

`NSExtensionPointIdentifier` identifies the virtual conference extension. `NSExtensionPrincipalClass` specifies a custom subclass of `EKVirtualConferenceProvider`. If you change the name of your custom subclass, update `NSExtensionPrincipalClass` with the new name.

`VirtualConferenceProvider`, a subclass of [`EKVirtualConferenceProvider`](ekvirtualconferenceprovider.md), provides an initial code that supports creating and adding a single conference room to an event in Calendar. `VirtualConferenceProvider` implements the [`fetchAvailableRoomTypes(completionHandler:)`](ekvirtualconferenceprovider/fetchavailableroomtypes(completionhandler:).md) and [`fetchVirtualConference(identifier:completionHandler:)`](ekvirtualconferenceprovider/fetchvirtualconference(identifier:completionhandler:).md) methods. The former creates and returns a list with one conference room, and the latter creates and returns information about a virtual conference.

You can build and run the project before you customize the extension code. To customize the extension, the sample project extension overrides `fetchAvailableRoomTypes(completionHandler:)` and `fetchVirtualConference(identifier:completionHandler:)`.

##### Provide Room Details

The sample project extension provides a personal room and a one-time room that people can select in the calendar event to schedule a virtual conference. It creates an [`EKVirtualConferenceRoomTypeDescriptor`](ekvirtualconferenceroomtypedescriptor.md) object for each room. Each descriptor specifies a title and a unique identifier for the room:

```swift
let personalRoom = EKVirtualConferenceRoomTypeDescriptor(title: "Personal Room", identifier: "personal-room")
let oneTimeRoom = EKVirtualConferenceRoomTypeDescriptor(title: "One-Time Room", identifier: "onetime-room")
```

Then the sample project extension modifies the [`fetchAvailableRoomTypes(completionHandler:)`](ekvirtualconferenceprovider/fetchavailableroomtypes(completionhandler:).md) method to return a list that contains these rooms:

```swift
override func fetchAvailableRoomTypes() async throws -> [EKVirtualConferenceRoomTypeDescriptor] {
   // Create the different room types the app supports.
   let personalRoom = EKVirtualConferenceRoomTypeDescriptor(title: "Personal Room", identifier: "personal-room")
   let oneTimeRoom = EKVirtualConferenceRoomTypeDescriptor(title: "One-Time Room", identifier: "onetime-room")
    
   // A list of virtual rooms people can select in the calendar event.
   return [personalRoom, oneTimeRoom]
}
```

##### Create a Conference Descriptor

The sample project extension calls a custom method to set up a virtual conference descriptor for each of the rooms it provides. It creates a list of URL descriptors, including an HTTP URL universal link for joining the conference and an optional secondary URL for dialing in to the conference:

```swift
/*
     The sample project extension provides a primary URL to join this conference and an optional alternate URL
     to let people dial in to the conference.
 */
 var urlDescriptors = [EKVirtualConferenceURLDescriptor(title: "Join Meeting", url: url)]
        
if let alternateURL {
   urlDescriptors.append(EKVirtualConferenceURLDescriptor(title: "Audio Only", url: alternateURL))
}
```

Then the sample project extension creates an [`EKVirtualConferenceDescriptor`](ekvirtualconferencedescriptor.md) object that takes a specified name, the list of URL descriptors, and conference details:

```swift
// A descriptor that includes a title, a list of URL descriptors, and information about the conference.
 let virtualConferenceDescriptor = EKVirtualConferenceDescriptor(title: title, urlDescriptors: urlDescriptors, conferenceDetails: details)
```

##### Provide Conference Details

After a person selects the personal room or one-time room from the list in the calendar event, the system calls the [`fetchVirtualConference(identifier:completionHandler:)`](ekvirtualconferenceprovider/fetchvirtualconference(identifier:completionhandler:).md) method to fetch details about the room using its unique identifier.

The sample project extension uses this identifier to determine which virtual conference descriptor to create and provide. For example, if the identifier identifies the personal room, the sample project extension creates and configures a virtual conference descriptor that includes a name, a URL for joining the conference, and a generic message about the conference. If the identifier identifies the one-time room, the sample project extension creates and configures a virtual conference descriptor that includes a name, a URL for joining the conference, a phone number for dialing in to the conference, and reading material for the conference.

```swift
override func fetchVirtualConference(identifier: EKVirtualConferenceRoomTypeIdentifier) async throws -> EKVirtualConferenceDescriptor {
    let meetingID = UUID().uuidString.prefix(8).lowercased()
         
    // The identifier determines which conference the sample project extension sets up and returns.
    switch identifier {
    case "personal-room":
        let personalRoomDescriptor = createVirtualConferenceDescriptor(with: "Personal Room",
                                                                       url: URL(string: "https://www.personal.example.com/\(meetingID)")!,
                                                                       details: "Please join the meeting in my personal room.")
        return personalRoomDescriptor
    case "onetime-room":
        let details = "For the topic, see the documentation at https://developer.apple.com/documentation/eventkit/ekvirtualconferenceprovider"
        let oneTimeRoomDescriptor = createVirtualConferenceDescriptor(with: "One-Time Room",
                                                                      url: URL(string: "https://www.team.example.com/\(meetingID)")!,
                                                                      alternateURL: URL(string: "tel:1-408-555-0100"),
                                                                      details: details)
            
        return oneTimeRoomDescriptor
    // If the identifier is unknown, the sample project extension throws an error to indicate an invalid room.
    default:
        throw VirtualConferenceSampleError.invalidRoom(identifier)
    }
}
```

## See Also

- [class EKVirtualConferenceProvider](ekvirtualconferenceprovider.md)
  An object that associates virtual conferencing details with an event object in a user’s calendar.
- [class EKVirtualConferenceDescriptor](ekvirtualconferencedescriptor.md)
  Details about a virtual conference that uses a custom room type.
- [class EKVirtualConferenceRoomTypeDescriptor](ekvirtualconferenceroomtypedescriptor.md)
  Details about a room where virtual conferences take place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/implementing-a-virtual-conference-extension)*