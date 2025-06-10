# nw_path_get_link_quality(_:)

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
func nw_path_get_link_quality(_ path: nw_path_t) -> nw_link_quality_t
```

#### Return Value

Returns the link quality measurement of the link layer network attachment. Returns nw_link_quality_unknown if there is no measurement available.

#### Discussion

```None
Fetches the link quality measurement for the interface.
```

## Parameters

- `path`: The path object to check.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_path_get_link_quality(_:))*