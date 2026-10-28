# nw_parameters_get_allow_ultra_constrained(_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

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
func nw_parameters_get_allow_ultra_constrained(_ parameters: nw_parameters_t) -> Bool
```

```c
bool nw_parameters_get_allow_ultra_constrained(nw_parameters_t parameters);
```

## Return Value

Returns whether or not ultra-constrained interfaces are allowed.

## Discussion

Check if the parameters explicitly allow connectivity over ultra-constrained interfaces.

## Parameters

- `parameters`: The parameters to check.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_parameters_get_allow_ultra_constrained(_:))*