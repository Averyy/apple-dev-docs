# nw_parameters_attribution_t

**Framework**: Network  
**Kind**: enum

The entities that can make a network request.

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
enum nw_parameters_attribution_t
```

#### Overview

Use one of these values when setting the `attribution` parameter of a network request with the [`nw_parameters_get_attribution(_:)`](nw_parameters_get_attribution(_:).md) method. If you don’t set a value, the system assumes [`nw_parameters_attribution_t.developer`](nw_parameters_attribution_t/developer.md).

## Topics

### Request Sources
- [nw_parameters_attribution_t.developer](nw_parameters_attribution_t/developer.md)
  A developer-initiated network request.
- [nw_parameters_attribution_t.user](nw_parameters_attribution_t/user.md)
  The user explicitly directs the app to make a network request.
### Initializers
- [init?(rawValue: UInt8)](nw_parameters_attribution_t/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Inspecting app activity data](inspecting-app-activity-data.md)
  Verify that your app accesses only the user data and network resources that you expect it to access.
- [Indicating the source of network activity](indicating-the-source-of-network-activity.md)
  Control whether the App Privacy Report attributes network traffic to the app or to the user.
- [func nw_parameters_set_attribution(nw_parameters_t, nw_parameters_attribution_t)](nw_parameters_set_attribution(_:_:).md)
  Sets a flag that indicates whether the network request originates from the developer or the user.
- [func nw_parameters_get_attribution(nw_parameters_t) -> nw_parameters_attribution_t](nw_parameters_get_attribution(_:).md)
  Gets a flag that indicates whether the network request originates from the developer or the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_parameters_attribution_t)*