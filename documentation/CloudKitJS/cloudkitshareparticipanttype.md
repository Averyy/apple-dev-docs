# CloudKit.ShareParticipantType

**Framework**: CloudKit JS  
**Kind**: enum

Determines whether a participant can modify the list of participants of a shared record.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
interface CloudKit.ShareParticipantType {
	const String UNKNOWN;
	const String PRIVATE_USER;
	const String PUBLIC_USER;
	const String OWNER;
};
```

## Topics

### Enumeration Cases
- [OWNER](cloudkit.shareparticipanttype/owner.md)
  The owner of the shared record who can add private users but not add public users.
- [PRIVATE_USER](cloudkit.shareparticipanttype/private_user.md)
  Participants who were invited to share the record by the owner.
- [PUBLIC_USER](cloudkit.shareparticipanttype/public_user.md)
  Participants who accepted a shared record by accessing the share URL.
- [UNKNOWN](cloudkit.shareparticipanttype/unknown.md)
  Unknown type of participant.

## See Also

- [CloudKit.AppleIDButtonTheme](cloudkit.appleidbuttontheme.md)
  Specifies the look of the Apple ID button.
- [CloudKit.DatabaseScope](cloudkit.databasescope.md)
  Available database scopes.
- [CloudKit.QueryFilterComparator](cloudkit.queryfiltercomparator.md)
  The comparators you use to create queries.
- [CloudKit.ReferenceAction](cloudkit.referenceaction.md)
  The delete action for a reference object.
- [CloudKit.ShareParticipantAcceptanceStatus](cloudkit.shareparticipantacceptancestatus.md)
  The status of a participant accepting a share invitation.
- [CloudKit.ShareParticipantPermission](cloudkit.shareparticipantpermission.md)
  The status of a participant accepting a share invitation.
- [CloudKit.SubscriptionType](cloudkit.subscriptiontype.md)
  The type of subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.shareparticipanttype)*