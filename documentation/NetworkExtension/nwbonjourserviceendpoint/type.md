# type

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The endpoint’s Bonjour service type.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_endpoint_get_bonjour_service_type(_:)`](../../Network/nw_endpoint_get_bonjour_service_type%28_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
var type: String { get }
```

```objc
@property (nonatomic, readonly) NSString * type;
```

## Discussion

For example, the service type could be `"_music._tcp"`.

## See Also

### Getting endpoint properties
- [var name: String](./name.md)
  The endpoint’s Bonjour service name.
- [var domain: String](./domain.md)
  The endpoint’s Bonjour service domain, such as `"local"`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwbonjourserviceendpoint/type)*