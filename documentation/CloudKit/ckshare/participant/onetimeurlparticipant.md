# oneTimeURLParticipant()

**Framework**: CloudKit  
**Kind**: method

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

When a participant’s email address / phone number / userRecordID isn’t known up-front, a @c oneTimeURLParticipant can be added to the share. Once the share is saved, a custom invitation link is available for that @c oneTimeURLParticipant. The link is accessed via `-[CKShare oneTimeURLForParticipantID]:)`. This custom link can be used by any recipient user to fetch share metadata and accept the share.

Note that a one-time URL participant in the @c CKShareParticipantAcceptanceStatusPending state has empty `CKUserIdentity.nameComponents` and a nil `CKUserIdentity.lookupInfo`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/participant/onetimeurlparticipant())*