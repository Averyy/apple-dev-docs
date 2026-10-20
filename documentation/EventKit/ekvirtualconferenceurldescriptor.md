# EKVirtualConferenceURLDescriptor

**Framework**: EventKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface EKVirtualConferenceURLDescriptor : NSObject
```

#### Overview

To let users join a virtual conference, you provide one or more URL descriptor objects in the [`EKVirtualConferenceDescriptor`](./ekvirtualconferencedescriptor.md) for the conference. Calendar uses the first URL descriptor as the preferred way for users to join a virtual conference and displays any additional links you provide in the virtual conference details.

## Topics

### Creating URL Descriptors
- [init(title: String?, url: URL)](./ekvirtualconferenceurldescriptor/init%28title,url%29-8l9d9.md)
  Creates a URL descriptor with the given title and URL.
### Configuring URL Descriptors
- [var title: String?](./ekvirtualconferenceurldescriptor/title.md)
  The user-visible name of a room where virtual conferences take place, such as Personal Room or Team Room.
- [var url: URL](./ekvirtualconferenceurldescriptor/url.md)
  The URL that users open to join a virtual conference.
### Initializers
- [init(title: String?, URL: URL)](./ekvirtualconferenceurldescriptor/init%28title,url%29-alzy.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configuring Virtual Conferences
- [var title: String?](./ekvirtualconferencedescriptor/title.md)
  The user-visible name of the virtual conference.
- [var urlDescriptors: [EKVirtualConferenceURLDescriptor]](./ekvirtualconferencedescriptor/urldescriptors.md)
  An array that contains objects with details about where to join the virtual conference.
- [var conferenceDetails: String?](./ekvirtualconferencedescriptor/conferencedetails.md)
  Additional information about the conference that users may find helpful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekvirtualconferenceurldescriptor)*