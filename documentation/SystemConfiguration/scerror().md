# SCError()

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns an error or status code associated with the most recent function call.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func SCError() -> Int32
```

```c
int SCError();
```

## Return Value

The most recent status or error code generated as the result of calling a function defined by the System Configuration framework. See [Status and Error Codes](./api-1518026-status-and-error-codes.md) for descriptions of these codes.

## See Also

### Functions
- [func SCCopyLastError() -> CFError](./sccopylasterror%28%29.md)
  Returns an error or status code associated with the most recent function call.
- [func SCErrorString(Int32) -> UnsafePointer<CChar>](./scerrorstring%28_%29.md)
  Returns a string describing the specified status code or error code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scerror())*