# underlyingErrorsKey

**Framework**: ClassKit  
**Kind**: property  
**Role**: Type Property

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

```c
extern CLSErrorUserInfoKey const CLSErrorUnderlyingErrorsKey;
```

## Discussion

This key only appears for errors with code [`partialFailure`](../clserror/partialfailure.md) in Swift or [`CLSError.Code.partialFailure`](../clserror/code/partialfailure.md) in Objective-C, signifying that more than one error occurred.

## See Also

### Keys
- [static let objectKey: CLSErrorUserInfoKey](./objectkey.md)
  A key whose value is the object that caused the error.
- [static let successfulObjectsKey: CLSErrorUserInfoKey](./successfulobjectskey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clserroruserinfokey/underlyingerrorskey)*