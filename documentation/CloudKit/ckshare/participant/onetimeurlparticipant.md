# oneTimeURLParticipant()

**Framework**: CloudKit  
**Kind**: method

Generate a unique URL for inviting a participant without knowing their handle

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
class func oneTimeURLParticipant() -> Self
```

#### Discussion

When a participant’s email address / phone number / userRecordID isn’t known up-front, a [`oneTimeURLParticipant()`](ckshare/participant/onetimeurlparticipant().md) can be added to the share. Once the share is saved, a custom invitation link or one-time URL is available for the added participant via [`oneTimeURLForParticipantID:`](ckshare/onetimeurlforparticipantid:.md). This custom link can be used by any recipient user to fetch share metadata and accept the share.

Note that a one-time URL participant in the [`CKShare.ParticipantAcceptanceStatus.pending`](ckshare/participantacceptancestatus/pending.md) state has empty [`nameComponents`](ckuseridentity/namecomponents.md) and a nil [`lookupInfo`](ckuseridentity/lookupinfo-swift.property.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/participant/onetimeurlparticipant())*