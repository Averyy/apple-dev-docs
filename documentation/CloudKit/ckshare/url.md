# url

**Framework**: CloudKit  
**Kind**: property

The URL for inviting participants to the share.

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
var url: URL? { get }
```

#### Discussion

This property is only available after saving a share record to the server. This URL is stable and persists across shares and reshares of the same root record.

## See Also

- [var owner: CKShare.Participant](ckshare/owner.md)
  The participant that represents the share’s owner.
- [var currentUserParticipant: CKShare.Participant?](ckshare/currentuserparticipant.md)
  The participant that represents the current user.
- [var participants: [CKShare.Participant]](ckshare/participants.md)
  An array that contains the share’s participants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/url)*