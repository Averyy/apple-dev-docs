# nw_path_is_ultra_constrained(_:)

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
func nw_path_is_ultra_constrained(_ path: nw_path_t) -> Bool
```

#### Return Value

Returns true if the path uses any network interface that is considered ultra-constrained, false otherwise.

#### Discussion

```None
Checks if the path uses any network interfaces that are considered ultra-constrained.
```

## Parameters

- `path`: The path object to check.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_path_is_ultra_constrained(_:))*