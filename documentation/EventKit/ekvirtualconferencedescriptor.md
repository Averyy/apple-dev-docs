# EKVirtualConferenceDescriptor

**Framework**: EventKit  
**Kind**: class

Details about a virtual conference that uses a custom room type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class EKVirtualConferenceDescriptor
```

#### Overview

When users add events to their calendars and use one of the room types that your provider defines, EventKit requests a virtual conference descriptor from your provider. Each virtual conference descriptor contains:

- A user-visible name for the virtual conference
- One or more URLs that the users open to join the virtual conference
- Optional details about the conference that may be helpful to users

Calendar uses the first URL that you provide as the preferred way for users to join a virtual conference and displays additional URLs as links in the virtual conference details.

> ❗ **Important**:  Events that use your virtual conference descriptors may sync to other devices where your app isn’t installed. To support links to your virtual conference regardless of whether your app is installed, adopt universal links in your app. Universal links let you specify HTTP URLs that open your app if it’s installed or open a corresponding web page if it’s not. For more information about adopting universal links in your app, see [`Supporting universal links in your app`](https://developer.apple.com/documentation/Xcode/supporting-universal-links-in-your-app).

 Events that use your virtual conference descriptors may sync to other devices where your app isn’t installed. To support links to your virtual conference regardless of whether your app is installed, adopt universal links in your app. Universal links let you specify HTTP URLs that open your app if it’s installed or open a corresponding web page if it’s not. For more information about adopting universal links in your app, see [`Supporting universal links in your app`](https://developer.apple.com/documentation/Xcode/supporting-universal-links-in-your-app).

## Topics

### Creating Conference Descriptors
- [init(title: String?, urlDescriptors: [EKVirtualConferenceURLDescriptor], conferenceDetails: String?)](ekvirtualconferencedescriptor/init(title:urldescriptors:conferencedetails:).md)
  Creates an object that describes a virtual conference, including a name and URL to join the conference.
### Configuring Virtual Conferences
- [var title: String?](ekvirtualconferencedescriptor/title.md)
  The user-visible name of the virtual conference.
- [var urlDescriptors: [EKVirtualConferenceURLDescriptor]](ekvirtualconferencedescriptor/urldescriptors.md)
  An array that contains objects with details about where to join the virtual conference.
- [class EKVirtualConferenceURLDescriptor](ekvirtualconferenceurldescriptor.md)
  Details about how users join a virtual conference, including a title and URL.
- [var conferenceDetails: String?](ekvirtualconferencedescriptor/conferencedetails.md)
  Additional information about the conference that users may find helpful.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class EKVirtualConferenceProvider](ekvirtualconferenceprovider.md)
  An object that associates virtual conferencing details with an event object in a user’s calendar.
- [class EKVirtualConferenceRoomTypeDescriptor](ekvirtualconferenceroomtypedescriptor.md)
  Details about a room where virtual conferences take place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekvirtualconferencedescriptor)*