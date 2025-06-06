# nw_parameters_set_attribution(_:_:)

**Framework**: Network  
**Kind**: func

Sets a flag that indicates whether the network request originates from the developer or the user.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func nw_parameters_set_attribution(_ parameters: nw_parameters_t, _ attribution: nw_parameters_attribution_t)
```

## Mentions

- [Inspecting app activity data](inspecting-app-activity-data.md)
- [Indicating the source of network activity](indicating-the-source-of-network-activity.md)

#### Discussion

If you don’t set this flag, the system assumes a value of [`nw_parameters_attribution_t.developer`](nw_parameters_attribution_t/developer.md). Use this default value for any network request that your app makes that isn’t explicitly from the user. This includes requests that you make to your own server, even when you load user data. It also includes links that the user selects, but that you modify in any way — including by adding HTTP headers — before loading the content.

Set this value to [`nw_parameters_attribution_t.user`](nw_parameters_attribution_t/user.md) only for requests that the user explicitly makes, like when the user enters a URL or taps or clicks a URL that they can read, and only if your app loads and displays the data without altering the request.

## Parameters

- `parameters`: The network parameters to update.
- `attribution`: An indication of whether the network request comes from the developer or from the user.

## See Also

- [Inspecting app activity data](inspecting-app-activity-data.md)
  Verify that your app accesses only the user data and network resources that you expect it to access.
- [Indicating the source of network activity](indicating-the-source-of-network-activity.md)
  Control whether the App Privacy Report attributes network traffic to the app or to the user.
- [func nw_parameters_get_attribution(nw_parameters_t) -> nw_parameters_attribution_t](nw_parameters_get_attribution(_:).md)
  Gets a flag that indicates whether the network request originates from the developer or the user.
- [enum nw_parameters_attribution_t](nw_parameters_attribution_t.md)
  The entities that can make a network request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_parameters_set_attribution(_:_:))*