# try()

**Framework**: Foundation  
**Kind**: method

Attempts to acquire the receiver and immediately returns a Boolean value that indicates whether the attempt was successful.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func `try`() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the attempt to acquire the receiver was successful, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Raises `NSGenericException` if a file-system error occurs.

## See Also

- [func unlock()](nsdistributedlock/unlock.md)
  Relinquishes the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdistributedlock/try())*