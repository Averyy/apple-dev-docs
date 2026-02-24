# SCErrorString(_:)

**Framework**: System Configuration  
**Kind**: func

Returns a string describing the specified status code or error code.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func SCErrorString(_ status: Int32) -> UnsafePointer<CChar>
```

#### Return Value

The message string associated with the status or error identified by `status`.

## Parameters

- `status`: A status or error code described in [`Status and Error Codes`](1518026-status-and-error-codes.md). You typically get this code by calling [`SCError()`](scerror().md) or [`SCCopyLastError()`](sccopylasterror().md).

## See Also

- [func SCCopyLastError() -> CFError](sccopylasterror().md)
  Returns an error or status code associated with the most recent function call.
- [func SCError() -> Int32](scerror().md)
  Returns an error or status code associated with the most recent function call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scerrorstring(_:))*