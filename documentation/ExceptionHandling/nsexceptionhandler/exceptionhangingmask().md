# exceptionHangingMask()

**Framework**: Exception Handling  
**Kind**: method  
**Role**: Instance Method

Returns a bit mask representing the types of exceptions that will halt execution for debugging.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func exceptionHangingMask() -> Int
```

```objc
- (NSUInteger) exceptionHangingMask;
```

#### Return Value

A bit mask composed of one or more constants specifying the types of exceptions that will halt execution for debugging. See [System Hang Constants](../system-hang-constants.md) for information about the constants.

## See Also

### Getting and setting exception masks
- [func exceptionHandlingMask() -> Int](./exceptionhandlingmask%28%29.md)
  Returns a bit mask representing the types of exceptions monitored by the receiver and its handling and logging behavior.
- [func setExceptionHandlingMask(Int)](./setexceptionhandlingmask%28_%29.md)
  Sets the bit mask of constants specifying the types of exceptions monitored by the receiver and its handling and logging behavior.
- [func setExceptionHangingMask(Int)](./setexceptionhangingmask%28_%29.md)
  Sets the bit mask of constants specifying the types of exceptions that will halt execution for debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exceptionhandling/nsexceptionhandler/exceptionhangingmask())*