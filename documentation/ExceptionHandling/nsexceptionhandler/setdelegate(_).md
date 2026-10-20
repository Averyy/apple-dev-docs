# setDelegate(_:)

**Framework**: Exception Handling  
**Kind**: method  
**Role**: Instance Method

Sets the delegate of the `NSExceptionHandler` object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func setDelegate(_ anObject: Any!)
```

```objc
- (void) setDelegate:(id) anObject;
```

## Parameters

- `anObject`: The object to receive the delegation messages described in [NSExceptionHandlerDelegate](../nsexceptionhandlerdelegate.md)

## See Also

### Getting and setting the delegate
- [func delegate() -> Any!](./delegate%28%29.md)
  Returns the delegate of the `NSExceptionHandler` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exceptionhandling/nsexceptionhandler/setdelegate(_:))*