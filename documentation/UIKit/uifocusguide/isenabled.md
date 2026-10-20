# isEnabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the guide is focusable.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isEnabled) BOOL enabled;
```

#### Discussion

If the value of this property is [`true`](../../Swift/true.md) (the default), then the guide may be focusable. Some conditions, defined by the system, may prevent the guide from being focusable even if it’s enabled, such as when the guide’s frame overlaps with the currently focused view. However, if this property is set to [`false`](../../Swift/false.md), then the guide isn’t focusable.

## See Also

### Enabling focus
- [var preferredFocusEnvironments: [any UIFocusEnvironment]!](./preferredfocusenvironments.md)
  An array of focus environments to which the guide directs focus, ordered by priority.
- [var preferredFocusedView: UIView?](./preferredfocusedview.md)
  The view that the focus will be redirected to if this guide is focused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusguide/isenabled)*