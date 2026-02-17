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

When a participant’s email address / phone number / userRecordID isn’t known up-front, you can add a [`oneTimeURLParticipant()`](ckshare/participant/onetimeurlparticipant().md) to the share. Once you save the share, you can get a custom invitation link or one-time URL for the added participant via [`oneTimeURL(for:)`](ckshare/onetimeurl(for:).md). Any recipient user can use this custom link to fetch share metadata and accept the share.

Note that a one-time URL participant in the [`CKShare.ParticipantAcceptanceStatus.pending`](ckshare/participantacceptancestatus/pending.md) state has empty [`nameComponents`](ckuseridentity/namecomponents.md) and a nil [`lookupInfo`](ckuseridentity/lookupinfo-swift.property.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/participant/onetimeurlparticipant())*