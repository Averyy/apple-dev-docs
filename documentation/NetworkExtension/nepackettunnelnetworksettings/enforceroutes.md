# enforceRoutes

**Framework**: Network Extension  
**Kind**: property

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var enforceRoutes: Bool { get set }
```

#### Discussion

If YES, route rules for this tunnel will take precendence over any locally-defined routes. The default is NO. The enforceRoutes property in NEVPNProtocol class takes precedence if set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/enforceroutes)*