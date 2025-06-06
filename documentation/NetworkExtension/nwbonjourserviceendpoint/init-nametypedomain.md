# init(name:type:domain:)

**Framework**: Network Extension  
**Kind**: init

Create an endpoint with a Bonjour service name, type, and domain. All fields must be specified.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(name: String, type: String, domain: String)
```

#### Return Value

The new [`NWBonjourServiceEndpoint`](nwbonjourserviceendpoint.md) object.

## Parameters

- `name`: The Bonjour service name.
- `type`: The Bonjour service type.
- `domain`: The Bonjour service domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwbonjourserviceendpoint/init(name:type:domain:))*