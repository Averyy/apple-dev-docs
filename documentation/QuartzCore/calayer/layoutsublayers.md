# layoutSublayers()

**Framework**: Core Animation  
**Kind**: method

Tells the layer to update its layout.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func layoutSublayers()
```

#### Discussion

Subclasses can override this method and use it to implement their own layout algorithm. Your implementation must set the frame of each sublayer managed by the receiver.

The default implementation of this method calls the `layoutSublayers(of:)` method in Swift or `layoutSublayersOfLayer:` method in Objective-C of the layer’s delegate object. If there is no delegate object, or the delegate does not implement that method, this method calls the `layoutSublayers(of:)` method in Swift or `layoutSublayersOfLayer:` method in Objective-C of the object in the [`layoutManager`](calayer/layoutmanager.md) property.

## See Also

- [var layoutManager: (any CALayoutManager)?](calayer/layoutmanager.md)
  The object responsible for laying out the layer’s sublayers.
- [func setNeedsLayout()](calayer/setneedslayout.md)
  Invalidates the layer’s layout and marks it as needing an update.
- [func layoutIfNeeded()](calayer/layoutifneeded.md)
  Recalculate the receiver’s layout, if required.
- [func needsLayout() -> Bool](calayer/needslayout.md)
  Returns a Boolean indicating whether the layer has been marked as needing a layout update.
- [var autoresizingMask: CAAutoresizingMask](calayer/autoresizingmask.md)
  A bitmask defining how the layer is resized when the bounds of its superlayer changes.
- [func resize(withOldSuperlayerSize: CGSize)](calayer/resize(witholdsuperlayersize:).md)
  Informs the receiver that the size of its superlayer changed.
- [func resizeSublayers(withOldSize: CGSize)](calayer/resizesublayers(witholdsize:).md)
  Informs the receiver’s sublayers that the receiver’s size has changed.
- [func preferredFrameSize() -> CGSize](calayer/preferredframesize.md)
  Returns the preferred size of the layer in the coordinate space of its superlayer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/layoutsublayers())*