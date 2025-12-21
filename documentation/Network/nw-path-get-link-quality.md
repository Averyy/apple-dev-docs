# nw_path_get_link_quality(_:)

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
func nw_path_get_link_quality(_ path: nw_path_t) -> nw_link_quality_t
```

#### Return Value

Returns the link quality measurement of the link layer network attachment. Returns nw_link_quality_unknown if there is no measurement available.

#### Discussion

Fetches the link quality measurement for the interface. Link quality measurement is a representation of the expected capabilities of the link layer network attachment. Use this value to tune initial values for algorithms that can scale with the capabilities of the network. Do not use this value to gate connection attempts or to override adjustments that would be made based on actual network performance.

## Parameters

- `path`: The path object to check.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_path_get_link_quality(_:))*