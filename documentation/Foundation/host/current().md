# current()

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns an `NSHost` object representing the host the process is running on.

**Availability**:
- macOS 10.0+ - Deprecated in 27.2

> **Deprecated**: Use Network framework instead, see deprecation notice in <Foundation/NSHost.h>

## Declaration

```swift
class func current() -> Self
```

```objc
+ (instancetype) currentHost;
```

#### Return Value

`NSHost` object for the process’s host.

#### Discussion

This method executes synchronously. The execution time of this method can be highly variable, depending on the local network configuration, and may block for several seconds if the network is unreachable. To avoid blocking execution on the main thread, you should call this method in an [`Operation`](../operation.md) or *Grand Central Dispatch* block that executes asynchronously in the background.

## See Also

### Creating Hosts
- [convenience init(address: String)](./init%28address%29.md)
  Returns the `NSHost` with the Internet address `address`.
- [convenience init(name: String?)](./init%28name%29.md)
  Returns a host with a specific name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/host/current())*