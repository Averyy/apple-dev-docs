# init(name:type:domain:)

**Framework**: Network Extension  
**Kind**: init  
**Role**: Initializer

Create an endpoint with a Bonjour service name, type, and domain. All fields must be specified.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_endpoint_create_bonjour_service(_:_:_:)`](../../Network/nw_endpoint_create_bonjour_service%28_,_,_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
convenience init(name: String, type: String, domain: String)
```

```objc
+ (instancetype) endpointWithName:(NSString *) name type:(NSString *) type domain:(NSString *) domain;
```

#### Return Value

The new [`NWBonjourServiceEndpoint`](../nwbonjourserviceendpoint.md) object.

## Parameters

- `name`: The Bonjour service name.
- `type`: The Bonjour service type.
- `domain`: The Bonjour service domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwbonjourserviceendpoint/init(name:type:domain:))*