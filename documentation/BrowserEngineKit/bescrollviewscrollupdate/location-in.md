# location(in:)

**Framework**: BrowserEngineKit  
**Kind**: method

Returns the coordinates of the scroll update in the given view’s bounds.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
@MainActor
func location(in view: UIView?) -> CGPoint
```

#### Return Value

The location of the scroll update in the specified view.

## Parameters

- `view`: The view in which to find the scroll update location. Pass   to get the location in the window’s coordinate system.

## See Also

- [func translation(in: UIView?) -> CGPoint](bescrollviewscrollupdate/translation(in:).md)
  Returns the amount of scrolling in the scroll update in the given view’s coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bescrollviewscrollupdate/location(in:))*