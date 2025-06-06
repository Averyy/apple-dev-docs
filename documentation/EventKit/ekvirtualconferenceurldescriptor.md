# EKVirtualConferenceURLDescriptor

**Framework**: EventKit  
**Kind**: class

Details about how users join a virtual conference, including a title and URL.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class EKVirtualConferenceURLDescriptor
```

#### Overview

To let users join a virtual conference, you provide one or more URL descriptor objects in the [`EKVirtualConferenceDescriptor`](ekvirtualconferencedescriptor.md) for the conference. Calendar uses the first URL descriptor as the preferred way for users to join a virtual conference and displays any additional links you provide in the virtual conference details.

## Topics

### Creating URL Descriptors
- [init(title: String?, url: URL)](ekvirtualconferenceurldescriptor/init(title:url:).md)
  Creates a URL descriptor with the given title and URL.
### Configuring URL Descriptors
- [var title: String?](ekvirtualconferenceurldescriptor/title.md)
  The user-visible name of a room where virtual conferences take place, such as Personal Room or Team Room.
- [var url: URL](ekvirtualconferenceurldescriptor/url.md)
  The URL that users open to join a virtual conference.

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

- [var title: String?](ekvirtualconferencedescriptor/title.md)
  The user-visible name of the virtual conference.
- [var urlDescriptors: [EKVirtualConferenceURLDescriptor]](ekvirtualconferencedescriptor/urldescriptors.md)
  An array that contains objects with details about where to join the virtual conference.
- [var conferenceDetails: String?](ekvirtualconferencedescriptor/conferencedetails.md)
  Additional information about the conference that users may find helpful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekvirtualconferenceurldescriptor)*