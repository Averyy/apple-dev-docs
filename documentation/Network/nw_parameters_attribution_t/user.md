# nw_parameters_attribution_t.user

**Framework**: Network  
**Kind**: case

The user explicitly directs the app to make a network request.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case user
```

## Mentions

- [Indicating the source of network activity](indicating-the-source-of-network-activity.md)

#### Discussion

Use this value for the `attribution` parameter of a call to the [`nw_parameters_get_attribution(_:)`](nw_parameters_get_attribution(_:).md) method when constructing a network request that satisfies a user request to access an explicit, unmodified URL. In all other cases, use the [`nw_parameters_attribution_t.developer`](nw_parameters_attribution_t/developer.md) value instead.

## See Also

- [nw_parameters_attribution_t.developer](nw_parameters_attribution_t/developer.md)
  A developer-initiated network request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_parameters_attribution_t/user)*