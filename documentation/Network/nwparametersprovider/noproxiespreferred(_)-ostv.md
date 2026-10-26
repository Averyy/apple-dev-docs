# noProxiesPreferred(_:)

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method

Prefer not using proxies when making connections.

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
func noProxiesPreferred(_ noProxies: Bool) -> Self
```

#### Discussion

Attempt connections without using proxies, only using any configured proxies if the connection cannot otherwise be completed.

## Parameters

- `noProxies`: True if connections should not use proxies, false otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparametersprovider/noproxiespreferred(_:)-ostv)*