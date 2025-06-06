# translation(in:)

**Framework**: BrowserEngineKit  
**Kind**: method

Returns the amount of scrolling in the scroll update in the given view’s coordinates.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
@MainActor
func translation(in view: UIView?) -> CGPoint
```

#### Return Value

The amount of scrolling in the scroll update in the specified view.

#### Overview

If either the `x` or `y` value of the returned point is non-zero, then the scroll update represents a change large enough to be visible along that axis.

## Parameters

- `view`: The view in which to find the scroll amount. Pass   to get the amount in the window’s coordinate system.

## See Also

- [func location(in: UIView?) -> CGPoint](bescrollviewscrollupdate/location(in:).md)
  Returns the coordinates of the scroll update in the given view’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bescrollviewscrollupdate/translation(in:))*