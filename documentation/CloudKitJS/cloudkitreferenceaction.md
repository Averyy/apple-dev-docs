# CloudKit.ReferenceAction

**Framework**: CloudKit JS  
**Kind**: enum

The delete action for a reference object.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
interface CloudKit.ReferenceAction {
	const String NONE;
	const String DELETE_SELF;
};
```

## Topics

### Enumeration Cases
- [DELETE_SELF](cloudkit.referenceaction/delete_self.md)
  No action when a referenced record is deleted.
- [NONE](cloudkit.referenceaction/none.md)
  Deletes a source record when the target record is deleted.

## See Also

- [CloudKit.AppleIDButtonTheme](cloudkit.appleidbuttontheme.md)
  Specifies the look of the Apple ID button.
- [CloudKit.DatabaseScope](cloudkit.databasescope.md)
  Available database scopes.
- [CloudKit.QueryFilterComparator](cloudkit.queryfiltercomparator.md)
  The comparators you use to create queries.
- [CloudKit.ShareParticipantAcceptanceStatus](cloudkit.shareparticipantacceptancestatus.md)
  The status of a participant accepting a share invitation.
- [CloudKit.ShareParticipantPermission](cloudkit.shareparticipantpermission.md)
  The status of a participant accepting a share invitation.
- [CloudKit.ShareParticipantType](cloudkit.shareparticipanttype.md)
  Determines whether a participant can modify the list of participants of a shared record.
- [CloudKit.SubscriptionType](cloudkit.subscriptiontype.md)
  The type of subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.referenceaction)*