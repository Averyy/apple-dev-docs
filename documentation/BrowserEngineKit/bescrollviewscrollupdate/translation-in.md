# translation(in:)

**Framework**: BrowserEngineKit  
**Kind**: method

Returns the scroll displacement in the coordinate system of the view that the update represents.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func translation(in view: UIView?) -> CGPoint
```

#### Return Value

The scroll displacement of the update in the specified view’s coordinate system.

#### Discussion

A nonzero `x` or `y` value in the returned point indicates a displacement large enough to produce a visible change along that axis.

## Parameters

- `view`: The view that contains the coordinate system to express the displacement. Pass `nil` to get the displacement in the window’s coordinate system.

## See Also

- [func location(in: UIView?) -> CGPoint](bescrollviewscrollupdate/location(in:).md)
  Returns the location of the scroll update in the coordinate system of the given view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bescrollviewscrollupdate/translation(in:))*