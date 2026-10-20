# layoutSublayers()

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) layoutSublayers;
```

#### Discussion

Subclasses can override this method and use it to implement their own layout algorithm. Your implementation must set the frame of each sublayer managed by the receiver.

The default implementation of this method calls the `layoutSublayers(of:)` method in Swift or `layoutSublayersOfLayer:` method in Objective-C of the layer’s delegate object. If there is no delegate object, or the delegate does not implement that method, this method calls the `layoutSublayers(of:)` method in Swift or `layoutSublayersOfLayer:` method in Objective-C of the object in the [`layoutManager`](./layoutmanager.md) property.

## See Also

### Managing layer resizing and layout
- [var layoutManager: (any CALayoutManager)?](./layoutmanager.md)
  The object responsible for laying out the layer’s sublayers.
- [func setNeedsLayout()](./setneedslayout%28%29.md)
  Invalidates the layer’s layout and marks it as needing an update.
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
- [func preferredFrameSize() -> CGSize](./preferredframesize%28%29.md)
  Returns the preferred size of the layer in the coordinate space of its superlayer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/layoutsublayers())*