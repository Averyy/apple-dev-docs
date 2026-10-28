# location(in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the location of the touch that started the interaction.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func location(in coordinateSpace: (any UICoordinateSpace)?) -> CGPoint
```

```objc
- (CGPoint) locationInCoordinateSpace:(id<UICoordinateSpace>) coordinateSpace;
```

## Return Value

The [`CGPoint`](../../CoreFoundation/cgpoint.md) that represents the current location of the touch, translated into the requested coordinate space.

## Discussion

Use this method to establish the current location of the touch that triggered the preview interaction.

> **Note**:  [`UIView`](../uiview.md) adopts the [`UICoordinateSpace`](../uicoordinatespace.md) protocol, so you can find the touch location within a view in the view hierarchy.

When the preview interaction isn’t running, calling this method returns an invalid point. You must therefore only call this method in response to one of the delegate callbacks specified in [`UIPreviewInteractionDelegate`](../uipreviewinteractiondelegate.md).

## Parameters

- `coordinateSpace`: The coordinate space in which the touch location should be returned.

## See Also

### Handling preview interactions
- [var view: UIView?](./view.md)
  The view from which the preview interaction receives touch events.
- [func cancel()](./cancel%28%29.md)
  Cancels the current preview interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewinteraction/location(in:))*