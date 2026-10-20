# conferenceDetails

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

Additional information about the conference that users may find helpful.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var conferenceDetails: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * conferenceDetails;
```

## See Also

### Configuring Virtual Conferences
- [var title: String?](./title.md)
  The user-visible name of the virtual conference.
- [var urlDescriptors: [EKVirtualConferenceURLDescriptor]](./urldescriptors.md)
  An array that contains objects with details about where to join the virtual conference.
- [class EKVirtualConferenceURLDescriptor](../ekvirtualconferenceurldescriptor.md)
  Details about how users join a virtual conference, including a title and URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekvirtualconferencedescriptor/conferencedetails)*