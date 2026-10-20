# setExceptionHangingMask(_:)

**Framework**: Exception Handling  
**Kind**: method  
**Role**: Instance Method

Sets the bit mask of constants specifying the types of exceptions that will halt execution for debugging.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func setExceptionHangingMask(_ aMask: Int)
```

```objc
- (void) setExceptionHangingMask:(NSUInteger) aMask;
```

## Parameters

- `aMask`: A bit mask composed of one or more constants specifying the types of exceptions that will halt execution for debugging. You specify multiple constants by performing a bitwise-OR operation. See [System Hang Constants](../system-hang-constants.md) for information about the constants.

## See Also

### Getting and setting exception masks
- [func exceptionHandlingMask() -> Int](./exceptionhandlingmask%28%29.md)
  Returns a bit mask representing the types of exceptions monitored by the receiver and its handling and logging behavior.
- [func exceptionHangingMask() -> Int](./exceptionhangingmask%28%29.md)
  Returns a bit mask representing the types of exceptions that will halt execution for debugging.
- [func setExceptionHandlingMask(Int)](./setexceptionhandlingmask%28_%29.md)
  Sets the bit mask of constants specifying the types of exceptions monitored by the receiver and its handling and logging behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exceptionhandling/nsexceptionhandler/setexceptionhangingmask(_:))*