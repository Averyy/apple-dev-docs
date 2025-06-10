# fetchVirtualConference(identifier:completionHandler:)

**Framework**: EventKit  
**Kind**: method

Provides details about a virtual conference that takes place in a room the user selects.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func fetchVirtualConference(identifier: EKVirtualConferenceRoomTypeIdentifier) async throws -> EKVirtualConferenceDescriptor
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func fetchVirtualConference(identifier: EKVirtualConferenceRoomTypeIdentifier) async throws -> EKVirtualConferenceDescriptor
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

To add calendar events using your virtual conference services, EventKit calls this method to retrieve the details for a virtual conference, including how a user joins the virtual conference. The room type identifier is one that your provider identified in a previous call to [`fetchAvailableRoomTypes(completionHandler:)`](ekvirtualconferenceprovider/fetchavailableroomtypes(completionhandler:).md).

```swift
override func fetchVirtualConference(identifier: EKVirtualConferenceRoomTypeIdentifier, completionHandler: @escaping (EKVirtualConferenceDescriptor?, Error?) -> Void) {
    let title: String
    let primaryURL: URL
    let dialInURL: URL
    let details: String
    
    // Configure the title, primary URL, an audio-only dial in phone
    // number, and some additional details for the room that the user
    // selected for the conference.
    switch identifier {
    case "personal-room":
        title = "Maria's Room"
        primaryURL = URL(string: "https://www.example.com/mruiz2")!
        dialInURL = URL(string: "tel:1-408-555-1111")!
        details = "Please join the meeting in my personal room."
    case "team-room":
        title = "Team Room"
        primaryURL = URL(string: "https://www.example.com/teamevents")!
        dialInURL = URL(string: "tel:1-408-555-9999")!
        details = "Please join the meeting in our team room."
    default:
        // If the room identifier is unknown, call the completion handler
        // with a nil array and a custom error that indicates the room is
        // invalid.
        completionHandler(nil, ProviderError.invalidRoom)
        return
    }
    
    // Create URL descriptors for the options to join the conference. In
    // this case, the primary option is an HTTP URL Universal Link the
    // works even if the app isn't installed. The extension also provides a
    // secondary tel URL to let people dial into the conference.
    let urlDescriptor = EKVirtualConferenceURLDescriptor(title: title, url: primaryURL)
    let alternate = EKVirtualConferenceURLDescriptor(title: "Audio Only", url: dialInURL)
    let urlDescriptors = [urlDescriptor, alternate]
    
    // Create a descriptor for the conference and call the completion
    // handler.
    let descriptor = EKVirtualConferenceDescriptor(
        title: title,
        urlDescriptors: urlDescriptors,
        conferenceDetails: details
    )
    completionHandler(descriptor, nil)
}
```

If your provider is unable to provide the virtual conference details, call the completion handler with `nil` for the first parameter and specify an error with a description of why the information isn’t available.

## Parameters

- `identifier`: The identifier for the room that the user chose for the virtual conference.
- `completionHandler`: A completion handler that you call after you determine the available rooms. If you provide a virtual conference descriptor, pass   for the error parameter. Conversely, if you provide an error object, pass   for the virtual conference descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekvirtualconferenceprovider/fetchvirtualconference(identifier:completionhandler:))*