# CloudKit.ShareParticipantAcceptanceStatus

**Framework**: CloudKit JS  
**Kind**: enum

The status of a participant accepting a share invitation.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
interface CloudKit.ShareParticipantAcceptanceStatus {
	const String UNKNOWN;
	const String PENDING;
	const String ACCEPTED;
};
```

## Topics

### Enumeration Cases
- [ACCEPTED](cloudkit.shareparticipantacceptancestatus/accepted.md)
  The participant accepted the invitation.
- [PENDING](cloudkit.shareparticipantacceptancestatus/pending.md)
  The participant was invited but hasn’t accepted.
- [UNKNOWN](cloudkit.shareparticipantacceptancestatus/unknown.md)
  The status is unknown.

## See Also

- [CloudKit.AppleIDButtonTheme](cloudkit.appleidbuttontheme.md)
  Specifies the look of the Apple ID button.
- [CloudKit.DatabaseScope](cloudkit.databasescope.md)
  Available database scopes.
- [CloudKit.QueryFilterComparator](cloudkit.queryfiltercomparator.md)
  The comparators you use to create queries.
- [CloudKit.ReferenceAction](cloudkit.referenceaction.md)
  The delete action for a reference object.
- [CloudKit.ShareParticipantPermission](cloudkit.shareparticipantpermission.md)
  The status of a participant accepting a share invitation.
- [CloudKit.ShareParticipantType](cloudkit.shareparticipanttype.md)
  Determines whether a participant can modify the list of participants of a shared record.
- [CloudKit.SubscriptionType](cloudkit.subscriptiontype.md)
  The type of subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.shareparticipantacceptancestatus)*