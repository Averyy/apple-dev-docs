# setNeedsLayout()

**Framework**: Core Animation  
**Kind**: method

Invalidates the layer’s layout and marks it as needing an update.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setNeedsLayout()
```

#### Discussion

You can call this method to indicate that the layout of a layer’s sublayers has changed and must be updated. The system typically calls this method automatically when the layer’s bounds change or when sublayers are added or removed. In macOS, if your layer’s [`layoutManager`](calayer/layoutmanager.md) property contains an object that implements the `invalidateLayout(of:)` method in Swift or the `invalidateLayoutOfLayer:` method in Objective-C, the system calls that method too.

During the next update cycle, the system calls the [`layoutSublayers()`](calayer/layoutsublayers().md) method of any layers requiring layout updates.

## See Also

- [var layoutManager: (any CALayoutManager)?](calayer/layoutmanager.md)
  The object responsible for laying out the layer’s sublayers.
- [func layoutSublayers()](calayer/layoutsublayers.md)
  Tells the layer to update its layout.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/setneedslayout())*