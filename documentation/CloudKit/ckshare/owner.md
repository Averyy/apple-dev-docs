# owner

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The participant that represents the share’s owner.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var owner: CKShare.Participant { get }
```

```objc
@property (copy, readonly) CKShareParticipant * owner;
```

## See Also

### Accessing the Share’s Attributes
- [var currentUserParticipant: CKShare.Participant?](./currentuserparticipant.md)
  The participant that represents the current user.
- [var participants: [CKShare.Participant]](./participants.md)
  An array that contains the share’s participants.
- [var url: URL?](./url.md)
  The Uniform Resource Locator (URL) for inviting participants to the share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/owner)*