# location(in:)

**Framework**: BrowserEngineKit  
**Kind**: method

Returns the location of the scroll update in the coordinate system of the given view.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func location(in view: UIView?) -> CGPoint
```

#### Return Value

The location of the scroll update in the specified view’s coordinate system.

## Parameters

- `view`: The view that contains the coordinate system to express the location. Pass `nil` to get the location in the window’s coordinate system.

## See Also

- [func translation(in: UIView?) -> CGPoint](bescrollviewscrollupdate/translation(in:).md)
  Returns the scroll displacement in the coordinate system of the view that the update represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bescrollviewscrollupdate/location(in:))*