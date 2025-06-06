# layoutIfNeeded()

**Framework**: Core Animation  
**Kind**: method

Recalculate the receiver’s layout, if required.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func layoutIfNeeded()
```

#### Discussion

When this message is received, the layer’s super layers are traversed until a ancestor layer is found that does not require layout. Then layout is performed on the entire layer-tree beneath that ancestor.

## See Also

- [var layoutManager: (any CALayoutManager)?](calayer/layoutmanager.md)
  The object responsible for laying out the layer’s sublayers.
- [func setNeedsLayout()](calayer/setneedslayout.md)
  Invalidates the layer’s layout and marks it as needing an update.
- [func layoutSublayers()](calayer/layoutsublayers.md)
  Tells the layer to update its layout.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/layoutifneeded())*