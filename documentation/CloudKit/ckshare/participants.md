# participants

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

An array that contains the share’s participants.

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
var participants: [CKShare.Participant] { get }
```

```objc
@property (copy, readonly) NSArray<CKShareParticipant *> * participants;
```

#### Discussion

The property’s value contains all of the share’s participants that the current user has permissions to see. At a minimum, it includes the share’s owner and the current user.

## See Also

### Accessing the Share’s Attributes
- [var owner: CKShare.Participant](./owner.md)
  The participant that represents the share’s owner.
- [var currentUserParticipant: CKShare.Participant?](./currentuserparticipant.md)
  The participant that represents the current user.
- [var url: URL?](./url.md)
  The Uniform Resource Locator (URL) for inviting participants to the share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/participants)*