# modified

**Framework**: CloudKit JS  
**Kind**: property

Information about when the record was last modified. The properties of this object are: `timestamp` (`Number`), the time at which the record was created, and `user` (`String`), the ID of the user who modified the record. This field is used by the [`CloudKit.RecordsResponse`](cloudkit.recordsresponse.md) class. This value of this field is set by the server. Omit this key when saving a record.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
attribute Object modified;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.record/modified)*