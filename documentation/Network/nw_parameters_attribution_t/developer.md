# nw_parameters_attribution_t.developer

**Framework**: Network  
**Kind**: case

A developer-initiated network request.

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
case developer
```

#### Discussion

Use this value for the `attribution` parameter of a call to the [`nw_parameters_get_attribution(_:)`](nw_parameters_get_attribution(_:).md) method when creating a network request for any purpose other than when the user explicitly accesses a link. This includes requests that your app makes to get user data. This is the default value.

For cases where the user enters a URL, like in the navigation bar of a web browser, or taps or clicks a URL to load the content it represents, use the [`nw_parameters_attribution_t.user`](nw_parameters_attribution_t/user.md) value instead.

## See Also

- [nw_parameters_attribution_t.user](nw_parameters_attribution_t/user.md)
  The user explicitly directs the app to make a network request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_parameters_attribution_t/developer)*