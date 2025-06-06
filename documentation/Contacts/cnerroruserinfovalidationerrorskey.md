# CNErrorUserInfoValidationErrorsKey

**Framework**: Contacts  
**Kind**: var

An array of validation-related error objects.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let CNErrorUserInfoValidationErrorsKey: String
```

#### Discussion

An array of [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) objects for [`CNError.Code.validationMultipleErrors`](cnerror/code/validationmultipleerrors.md).

## See Also

- [let CNErrorUserInfoAffectedRecordsKey: String](cnerroruserinfoaffectedrecordskey.md)
  The contact, group, and container objects for which the error code applies.
- [let CNErrorUserInfoAffectedRecordIdentifiersKey: String](cnerroruserinfoaffectedrecordidentifierskey.md)
  String objects for which the error code applies.
- [let CNErrorUserInfoKeyPathsKey: String](cnerroruserinfokeypathskey.md)
  An array of key paths associated with a given error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnerroruserinfovalidationerrorskey)*