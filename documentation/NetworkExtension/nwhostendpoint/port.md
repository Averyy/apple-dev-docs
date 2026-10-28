# port

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The endpoint’s port, represented as a string.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_endpoint_get_port(_:)`](../../Network/nw_endpoint_get_port%28_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
var port: String { get }
```

```objc
@property (nonatomic, readonly) NSString * port;
```

## Discussion

Since the port is represented as a string, it is always represented in host byte order. If converting between byte fields and strings, make sure to use host byte ordering.

## See Also

### Getting endpoint properties
- [var hostname: String](./hostname.md)
  The endpoint’s hostname.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwhostendpoint/port)*