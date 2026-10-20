# name

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The endpoint’s Bonjour service name.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_endpoint_get_bonjour_service_name(_:)`](../../Network/nw_endpoint_get_bonjour_service_name%28_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
var name: String { get }
```

```objc
@property (nonatomic, readonly) NSString * name;
```

## See Also

### Getting endpoint properties
- [var type: String](./type.md)
  The endpoint’s Bonjour service type.
- [var domain: String](./domain.md)
  The endpoint’s Bonjour service domain, such as `"local"`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwbonjourserviceendpoint/name)*