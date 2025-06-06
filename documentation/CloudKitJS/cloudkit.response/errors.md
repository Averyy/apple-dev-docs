# errors

**Framework**: CloudKit JS  
**Kind**: property

Errors that occurred in the request.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
readonly attribute CloudKit.CKError[] errors;
```

#### Discussion

There’s one [`CKError`](cloudkit/ckerror.md) object for each individual operation that failed.

## See Also

- [hasErrors](cloudkit.response/haserrors.md)
  A Boolean value indicating whether errors occurred in the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.response/errors)*