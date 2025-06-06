# CNErrorUserInfoAffectedRecordsKey

**Framework**: Contacts  
**Kind**: var

The contact, group, and container objects for which the error code applies.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let CNErrorUserInfoAffectedRecordsKey: String
```

#### Discussion

An array of one or more [`CNContact`](cncontact.md), [`CNGroup`](cngroup.md), or [`CNContainer`](cncontainer.md) objects for which the error code applies.

## See Also

- [let CNErrorUserInfoAffectedRecordIdentifiersKey: String](cnerroruserinfoaffectedrecordidentifierskey.md)
  String objects for which the error code applies.
- [let CNErrorUserInfoValidationErrorsKey: String](cnerroruserinfovalidationerrorskey.md)
  An array of validation-related error objects.
- [let CNErrorUserInfoKeyPathsKey: String](cnerroruserinfokeypathskey.md)
  An array of key paths associated with a given error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnerroruserinfoaffectedrecordskey)*