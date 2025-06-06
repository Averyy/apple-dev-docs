# CloudKit.QueryFilterComparator

**Framework**: CloudKit JS  
**Kind**: enum

The comparators you use to create queries.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
interface CloudKit.QueryFilterComparator {
	const String EQUALS;
	const String NOT_EQUALS;
	const String LESS_THAN;
	const String LESS_THAN_OR_EQUALS;
	const String GREATER_THAN;
	const String GREATER_THAN_OR_EQUALS;
	const String NEAR;
	const String CONTAINS_ALL_TOKENS;
	const String IN;
	const String NOT_IN;
	const String CONTAINS_ANY_TOKENS;
	const String LIST_CONTAINS;
	const String LIST_CONTAINS_ANY;
	const String NOT_LIST_CONTAINS;
	const String NOT_LIST_CONTAINS_ANY;
	const String BEGINS_WITH;
	const String NOT_BEGINS_WITH;
	const String LIST_MEMBER_BEGINS_WITH;
	const String NOT_LIST_MEMBER_BEGINS_WITH;
	const String LIST_CONTAINS_ALL;
	const String NOT_LIST_CONTAINS_ALL;
};
```

## Topics

### Enumeration Cases
- [BEGINS_WITH](cloudkit.queryfiltercomparator/begins_with.md)
  Finds records with a string field that begins with a substring.
- [CONTAINS_ALL_TOKENS](cloudkit.queryfiltercomparator/contains_all_tokens.md)
  Finds records with text fields containing all tokens.
- [CONTAINS_ANY_TOKENS](cloudkit.queryfiltercomparator/contains_any_tokens.md)
  Finds records with text fields containing any token.
- [EQUALS](cloudkit.queryfiltercomparator/equals.md)
  The value on the left is equal to the value on the right.
- [GREATER_THAN](cloudkit.queryfiltercomparator/greater_than.md)
  The value on the left is greater than the value on the right.
- [GREATER_THAN_OR_EQUALS](cloudkit.queryfiltercomparator/greater_than_or_equals.md)
  The value on the left is greater than or equal to the value on the right.
- [IN](cloudkit.queryfiltercomparator/in.md)
  The value on the left is in the list on the right.
- [LESS_THAN](cloudkit.queryfiltercomparator/less_than.md)
  The value on the left is less than the value on the right.
- [LESS_THAN_OR_EQUALS](cloudkit.queryfiltercomparator/less_than_or_equals.md)
  The value on the left is less than or equal to the value on the right.
- [LIST_CONTAINS](cloudkit.queryfiltercomparator/list_contains.md)
  Finds records containing values in its list field.
- [LIST_CONTAINS_ALL](cloudkit.queryfiltercomparator/list_contains_all.md)
  Finds records containing all values in its list field.
- [LIST_CONTAINS_ANY](cloudkit.queryfiltercomparator/list_contains_any.md)
  Finds records that contain any of the values in its list field.
- [LIST_MEMBER_BEGINS_WITH](cloudkit.queryfiltercomparator/list_member_begins_with.md)
  Finds records containing a value as the first item in its list field.
- [NEAR](cloudkit.queryfiltercomparator/near.md)
  The location on the left is within the specified distance of the location on the right.
- [NOT_BEGINS_WITH](cloudkit.queryfiltercomparator/not_begins_with.md)
  Finds records with a string field that doesn’t begin with a substring.
- [NOT_EQUALS](cloudkit.queryfiltercomparator/not_equals.md)
  The value on the left is not equal to the value on the right.
- [NOT_IN](cloudkit.queryfiltercomparator/not_in.md)
  The value on the left is not in the list on the right.
- [NOT_LIST_CONTAINS](cloudkit.queryfiltercomparator/not_list_contains.md)
  Finds records not containing values not in its list field.
- [NOT_LIST_CONTAINS_ALL](cloudkit.queryfiltercomparator/not_list_contains_all.md)
  Finds records not containing all values in its list field.
- [NOT_LIST_CONTAINS_ANY](cloudkit.queryfiltercomparator/not_list_contains_any.md)
  Finds records not containing any of the values in its list field.
- [NOT_LIST_MEMBER_BEGINS_WITH](cloudkit.queryfiltercomparator/not_list_member_begins_with.md)
  Finds records not containing a value as the first item in its list field.

## See Also

- [CloudKit.AppleIDButtonTheme](cloudkit.appleidbuttontheme.md)
  Specifies the look of the Apple ID button.
- [CloudKit.DatabaseScope](cloudkit.databasescope.md)
  Available database scopes.
- [CloudKit.ReferenceAction](cloudkit.referenceaction.md)
  The delete action for a reference object.
- [CloudKit.ShareParticipantAcceptanceStatus](cloudkit.shareparticipantacceptancestatus.md)
  The status of a participant accepting a share invitation.
- [CloudKit.ShareParticipantPermission](cloudkit.shareparticipantpermission.md)
  The status of a participant accepting a share invitation.
- [CloudKit.ShareParticipantType](cloudkit.shareparticipanttype.md)
  Determines whether a participant can modify the list of participants of a shared record.
- [CloudKit.SubscriptionType](cloudkit.subscriptiontype.md)
  The type of subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.queryfiltercomparator)*