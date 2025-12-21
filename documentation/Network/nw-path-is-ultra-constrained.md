# nw_path_is_ultra_constrained(_:)

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
func nw_path_is_ultra_constrained(_ path: nw_path_t) -> Bool
```

#### Return Value

Returns true if the path uses any network interface that is considered ultra-constrained, false otherwise.

#### Discussion

Checks if the path uses any network interfaces that are considered ultra-constrained.

## Parameters

- `path`: The path object to check.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_path_is_ultra_constrained(_:))*