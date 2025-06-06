# messageIdentifier

**Framework**: Group Activities  
**Kind**: property  
**Required**: Yes

A custom identification string for the current type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static var messageIdentifier: String { get }
```

#### Discussion

The string you return from this property must be unique among your app’s custom message types. When you send a message, [`GroupSessionMessenger`](groupsessionmessenger.md) includes this string in the data it sends to other devices. When it receives a message, [`GroupSessionMessenger`](groupsessionmessenger.md) creates the type that contains the matching string in this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/custommessageidentifiable/messageidentifier)*