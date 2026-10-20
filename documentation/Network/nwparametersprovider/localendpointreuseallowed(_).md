# localEndpointReuseAllowed(_:)

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Allow local endpoint reuse.

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
func localEndpointReuseAllowed(_ allowed: Bool) -> Self
```

#### Discussion

Allow multiple connections to use the same local address and port (`SO_REUSEADDR` and `SO_REUSEPORT`).

## Parameters

- `allowed`: True if allowed, false otherwise.

## Default Implementations

### NWParametersProvider Implementations
- [func localEndpointReuseAllowed(Bool) -> Self](./localendpointreuseallowed%28_%29-1x9ep.md)
  Allow local endpoint reuse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparametersprovider/localendpointreuseallowed(_:))*