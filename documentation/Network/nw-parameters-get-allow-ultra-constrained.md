# nw_parameters_get_allow_ultra_constrained(_:)

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
func nw_parameters_get_allow_ultra_constrained(_ parameters: nw_parameters_t) -> Bool
```

#### Return Value

Returns whether or not ultra-constrained interfaces are allowed.

#### Discussion

```None
Check if the parameters explicitly allow connectivity over
ultra-constrained interfaces.
```

## Parameters

- `parameters`: The parameters to check.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_parameters_get_allow_ultra_constrained(_:))*