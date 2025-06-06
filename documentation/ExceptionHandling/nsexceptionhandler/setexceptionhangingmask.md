# setExceptionHangingMask(_:)

**Framework**: Exception Handling  
**Kind**: method

Sets the bit mask of constants specifying the types of exceptions that will halt execution for debugging.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func setExceptionHangingMask(_ aMask: Int)
```

## Parameters

- `aMask`: A bit mask composed of one or more constants specifying the types of exceptions that   will halt execution for debugging. You specify multiple constants by performing a   bitwise-OR operation. See   for   information about the constants.

## See Also

- [func exceptionHandlingMask() -> Int](nsexceptionhandler/exceptionhandlingmask.md)
  Returns a bit mask representing the types of exceptions monitored by the receiver and its handling and logging behavior.
- [func exceptionHangingMask() -> Int](nsexceptionhandler/exceptionhangingmask.md)
  Returns a bit mask representing the types of exceptions that will halt execution for debugging.
- [func setExceptionHandlingMask(Int)](nsexceptionhandler/setexceptionhandlingmask(_:).md)
  Sets the bit mask of constants specifying the types of exceptions monitored by the receiver and its handling and logging behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exceptionhandling/nsexceptionhandler/setexceptionhangingmask(_:))*