# hostname

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The endpoint’s hostname.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_endpoint_get_hostname(_:)`](../../Network/nw_endpoint_get_hostname%28_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
var hostname: String { get }
```

```objc
@property (nonatomic, readonly) NSString * hostname;
```

## See Also

### Getting endpoint properties
- [var port: String](./port.md)
  The endpoint’s port, represented as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwhostendpoint/hostname)*