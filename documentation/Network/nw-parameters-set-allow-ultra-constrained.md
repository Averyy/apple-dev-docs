# nw_parameters_set_allow_ultra_constrained(_:_:)

**Framework**: Network  
**Kind**: func

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
func nw_parameters_set_allow_ultra_constrained(_ parameters: nw_parameters_t, _ allow_ultra_constrained: Bool)
```

#### Discussion

Explicitly allow connectivity over ultra-constrained interfaces. Without this being set, connections are not allowed to use these interfaces.

## Parameters

- `parameters`: The parameters to modify.
- `allow_ultra_constrained`: Whether or not ultra-constrained interfaces are allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_parameters_set_allow_ultra_constrained(_:_:))*