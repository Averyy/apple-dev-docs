# preferredFrameSize()

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Returns the preferred size of the layer in the coordinate space of its superlayer.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func preferredFrameSize() -> CGSize
```

```objc
- (CGSize) preferredFrameSize;
```

## Return Value

The layer’s preferred frame size.

## Discussion

In macOS, the default implementation of this method calls the `preferredSize(of:)` method in Swift or the `preferredSizeOfLayer:` method in Objective-C of its layout manager—that is, the object in its [`layoutManager`](./layoutmanager.md) property. If that object does not exist or does not implement that method, this method returns the size of the layer’s current [`bounds`](./bounds.md) rectangle mapped into the coordinate space of its [`superlayer`](./superlayer.md).

## See Also

### Managing layer resizing and layout
- [var layoutManager: (any CALayoutManager)?](./layoutmanager.md)
  The object responsible for laying out the layer’s sublayers.
- [func setNeedsLayout()](./setneedslayout%28%29.md)
  Invalidates the layer’s layout and marks it as needing an update.
- [func layoutSublayers()](./layoutsublayers%28%29.md)
  Tells the layer to update its layout.
- [func layoutIfNeeded()](./layoutifneeded%28%29.md)
  Recalculate the receiver’s layout, if required.
- [func needsLayout() -> Bool](./needslayout%28%29.md)
  Returns a Boolean indicating whether the layer has been marked as needing a layout update.
- [var autoresizingMask: CAAutoresizingMask](./autoresizingmask.md)
  A bitmask defining how the layer is resized when the bounds of its superlayer changes.
- [func resize(withOldSuperlayerSize: CGSize)](./resize%28witholdsuperlayersize%29.md)
  Informs the receiver that the size of its superlayer changed.
- [func resizeSublayers(withOldSize: CGSize)](./resizesublayers%28witholdsize%29.md)
  Informs the receiver’s sublayers that the receiver’s size has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/preferredframesize())*