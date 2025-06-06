# underlyingErrorsKey

**Framework**: ClassKit  
**Kind**: property

A key whose value is the array of errors that contributed to this error.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let underlyingErrorsKey: CLSErrorUserInfoKey
```

#### Discussion

This key only appears for errors with code [`partialFailure`](clserror/partialfailure.md) in Swift or [`CLSError.Code.partialFailure`](clserror/code/partialfailure.md) in Objective-C, signifying that more than one error occurred.

## See Also

- [static let objectKey: CLSErrorUserInfoKey](clserroruserinfokey/objectkey.md)
  A key whose value is the object that caused the error.
- [static let successfulObjectsKey: CLSErrorUserInfoKey](clserroruserinfokey/successfulobjectskey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clserroruserinfokey/underlyingerrorskey)*