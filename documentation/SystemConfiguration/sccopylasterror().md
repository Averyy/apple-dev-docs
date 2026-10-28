# SCCopyLastError()

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns an error or status code associated with the most recent function call.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func SCCopyLastError() -> CFError
```

```c
CFErrorRefSCCopyLastError();
```

## Return Value

The most recent status or error code generated as the result of calling a function defined by the System Configuration framework. The code is represented by a Core Foundation `CFErrorRef` opaque type.

## Discussion

Call the [`CFErrorGetCode(_:)`](../CoreFoundation/cferrorgetcode%28_%29.md) function on the returned object to get the underlying error-code integer. See [Status and Error Codes](./api-1518026-status-and-error-codes.md) for descriptions of these codes. For more on `CFErrorRef` objects, see [`CFError`](../CoreFoundation/cferror.md).

## See Also

### Functions
- [func SCError() -> Int32](./scerror%28%29.md)
  Returns an error or status code associated with the most recent function call.
- [func SCErrorString(Int32) -> UnsafePointer<CChar>](./scerrorstring%28_%29.md)
  Returns a string describing the specified status code or error code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/sccopylasterror())*