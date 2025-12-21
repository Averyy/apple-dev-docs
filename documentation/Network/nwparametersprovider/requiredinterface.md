# requiredInterface(_:)

**Framework**: Network  
**Kind**: method  
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparametersprovider/requiredinterface(_:))*