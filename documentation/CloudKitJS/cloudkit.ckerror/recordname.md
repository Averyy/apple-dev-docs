# recordName

**Framework**: CloudKit JS  
**Kind**: property

The name of the record that the operation failed on.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
readonly attribute String recordName;
```

#### Discussion

This property value is `Undefined` if the error is unrelated to a record operation.

## See Also

- [subscriptionID](cloudkit.ckerror/subscriptionid.md)
  A string that is a unique identifier for the subscription where the error occurred.
- [zoneID](cloudkit.ckerror/zoneid.md)
  The record zone in the database where the error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.ckerror/recordname)*