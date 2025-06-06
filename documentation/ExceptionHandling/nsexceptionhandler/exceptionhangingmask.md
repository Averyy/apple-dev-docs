# exceptionHangingMask()

**Framework**: Exception Handling  
**Kind**: method

Returns a bit mask representing the types of exceptions that will halt execution for debugging.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func exceptionHangingMask() -> Int
```

#### Return Value

A bit mask composed of one or more constants specifying the types of exceptions that will halt execution for debugging. See [`System Hang Constants`](system-hang-constants.md) for information about the constants.

## See Also

- [func exceptionHandlingMask() -> Int](nsexceptionhandler/exceptionhandlingmask.md)
  Returns a bit mask representing the types of exceptions monitored by the receiver and its handling and logging behavior.
- [func setExceptionHandlingMask(Int)](nsexceptionhandler/setexceptionhandlingmask(_:).md)
  Sets the bit mask of constants specifying the types of exceptions monitored by the receiver and its handling and logging behavior.
- [func setExceptionHangingMask(Int)](nsexceptionhandler/setexceptionhangingmask(_:).md)
  Sets the bit mask of constants specifying the types of exceptions that will halt execution for debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exceptionhandling/nsexceptionhandler/exceptionhangingmask())*