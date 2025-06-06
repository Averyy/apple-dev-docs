# subscriptionID

**Framework**: CloudKit JS  
**Kind**: property

A string that is a unique identifier for the subscription where the error occurred.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
readonly attribute String subscriptionID;
```

#### Discussion

This property value is `Undefined` if the error is unrelated to a subscription operation.

## See Also

- [recordName](cloudkit.ckerror/recordname.md)
  The name of the record that the operation failed on.
- [zoneID](cloudkit.ckerror/zoneid.md)
  The record zone in the database where the error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.ckerror/subscriptionid)*