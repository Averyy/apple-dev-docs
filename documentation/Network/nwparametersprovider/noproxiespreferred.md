# noProxiesPreferred(_:)

**Framework**: Network  
**Kind**: method  
**Required**: Yes

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
func noProxiesPreferred(_ preferred: Bool) -> Self
```

#### Discussion

Attempt connections without using proxies, only using any configured proxies if the connection cannot otherwise be completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparametersprovider/noproxiespreferred(_:))*