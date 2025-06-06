# SCError()

**Framework**: System Configuration  
**Kind**: func

Returns an error or status code associated with the most recent function call.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func SCError() -> Int32
```

#### Return Value

The most recent status or error code generated as the result of calling a function defined by the System Configuration framework. See [`Status and Error Codes`](1518026-status-and-error-codes.md) for descriptions of these codes.

## See Also

- [func SCCopyLastError() -> CFError](sccopylasterror().md)
  Returns an error or status code associated with the most recent function call.
- [func SCErrorString(Int32) -> UnsafePointer<CChar>](scerrorstring(_:).md)
  Returns a string describing the specified status code or error code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scerror())*