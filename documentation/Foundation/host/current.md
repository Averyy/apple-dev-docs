# current()

**Framework**: Foundation  
**Kind**: method

Returns an `NSHost` object representing the host the process is running on.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class func current() -> Self
```

#### Return Value

`NSHost` object for the process’s host.

#### Discussion

This method executes synchronously. The execution time of this method can be highly variable, depending on the local network configuration, and may block for several seconds if the network is unreachable. To avoid blocking execution on the main thread, you should call this method in an [`Operation`](operation.md) or  block that executes asynchronously in the background.

## See Also

- [convenience init(address: String)](host/init(address:).md)
  Returns the `NSHost` with the Internet address `address`.
- [convenience init(name: String?)](host/init(name:).md)
  Returns a host with a specific name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/host/current())*