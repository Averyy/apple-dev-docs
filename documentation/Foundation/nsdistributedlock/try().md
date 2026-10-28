# try()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Attempts to acquire the receiver and immediately returns a Boolean value that indicates whether the attempt was successful.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func `try`() -> Bool
```

```objc
- (BOOL) tryLock;
```

## Return Value

[`true`](../../Swift/true.md) if the attempt to acquire the receiver was successful, otherwise [`false`](../../Swift/false.md).

## Discussion

Raises `NSGenericException` if a file-system error occurs.

## See Also

### Related Documentation
- [func unlock()](./unlock%28%29.md)
  Relinquishes the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdistributedlock/try())*