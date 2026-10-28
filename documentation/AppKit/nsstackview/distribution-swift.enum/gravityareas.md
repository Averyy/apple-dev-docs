# NSStackView.Distribution.gravityAreas

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Stacked views will not have any special distribution behavior, relying on behavior described by gravity areas and set hugging priorities along the stacking axis.

**Availability**:
- macOS 10.11+

## Declaration

```swift
case gravityAreas
```

```c
NSStackViewDistributionGravityAreas
```

## Discussion

This is the default value.

## See Also

### Constants
- [NSStackView.Distribution.equalCentering](./equalcentering.md)
  Equal center-to-center spacing of the items is maintained as much as possible while still maintaining the minimum spacing between each view.
- [NSStackView.Distribution.equalSpacing](./equalspacing.md)
  The space separating stacked views along the stacking axis are maintained to be equal as much as possible while still maintaining the minimum spacing.
- [NSStackView.Distribution.fill](./fill.md)
  The effective hugging priority in the stacking axis is `NSLayoutPriorityRequired`, causing the stacked views to tightly fill the container along the stacking axis.
- [NSStackView.Distribution.fillEqually](./fillequally.md)
  Stacked views will have sizes maintained to be equal as much as possible along the stacking axis. The effective hugging priority in the stacking axis is `NSLayoutPriorityRequired`.
- [NSStackView.Distribution.fillProportionally](./fillproportionally.md)
  Stacked views will have sizes maintained to be equal, proportionally to their `intrinsicContentSize`s, as much as possible. The effective hugging priority in the stacking axis is `NSLayoutPriorityRequired`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/distribution-swift.enum/gravityareas)*