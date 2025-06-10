# nw_parameters_set_allow_ultra_constrained(_:_:)

**Framework**: Network  
**Kind**: func

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func nw_parameters_set_allow_ultra_constrained(_ parameters: nw_parameters_t, _ allow_ultra_constrained: Bool)
```

#### Discussion

```None
Explicitly allow connectivity over ultra-constrained interfaces. Without
this being set, connections are not allowed to use these interfaces.
```

## Parameters

- `parameters`: The parameters to modify.
- `allow_ultra_constrained`: Whether or not ultra-constrained interfaces are allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_parameters_set_allow_ultra_constrained(_:_:))*