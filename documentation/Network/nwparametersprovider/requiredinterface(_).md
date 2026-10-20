# requiredInterface(_:)

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Require an interface when connecting, listening, and browsing.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func requiredInterface(_ interface: NWInterface) -> Self
```

#### Discussion

Connections will fail if this interface is not available.

## Parameters

- `interface`: The interface to require.

## Default Implementations

### NWParametersProvider Implementations
- [func requiredInterface(NWInterface) -> Self](./requiredinterface%28_%29-tfqe.md)
  Require an interface when connecting, listening, and browsing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparametersprovider/requiredinterface(_:))*