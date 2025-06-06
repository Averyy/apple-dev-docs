# isEnabled

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the guide is focusable.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isEnabled: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/swift/true) (the default), then the guide may be focusable. Some conditions, defined by the system, may prevent the guide from being focusable even if it’s enabled, such as when the guide’s frame overlaps with the currently focused view. However, if this property is set to [`false`](https://developer.apple.com/documentation/swift/false), then the guide isn’t focusable.

## See Also

- [var preferredFocusEnvironments: [any UIFocusEnvironment]!](uifocusguide/preferredfocusenvironments.md)
  An array of focus environments to which the guide directs focus, ordered by priority.
- [var preferredFocusedView: UIView?](uifocusguide/preferredfocusedview.md)
  The view that the focus will be redirected to if this guide is focused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusguide/isenabled)*