# NSStackView.Distribution.fillProportionally

**Framework**: AppKit  
**Kind**: case

Stacked views will have sizes maintained to be equal, proportionally to their `intrinsicContentSize`s, as much as possible. The effective hugging priority in the stacking axis is `NSLayoutPriorityRequired`.

**Availability**:
- macOS 10.11+

## Declaration

```swift
case fillProportionally
```

## See Also

- [NSStackView.Distribution.equalCentering](nsstackview/distribution-swift.enum/equalcentering.md)
  Equal center-to-center spacing of the items is maintained as much as possible while still maintaining the minimum spacing between each view.
- [NSStackView.Distribution.equalSpacing](nsstackview/distribution-swift.enum/equalspacing.md)
  The space separating stacked views along the stacking axis are maintained to be equal as much as possible while still maintaining the minimum spacing.
- [NSStackView.Distribution.fill](nsstackview/distribution-swift.enum/fill.md)
  The effective hugging priority in the stacking axis is `NSLayoutPriorityRequired`, causing the stacked views to tightly fill the container along the stacking axis.
- [NSStackView.Distribution.fillEqually](nsstackview/distribution-swift.enum/fillequally.md)
  Stacked views will have sizes maintained to be equal as much as possible along the stacking axis. The effective hugging priority in the stacking axis is `NSLayoutPriorityRequired`.
- [NSStackView.Distribution.gravityAreas](nsstackview/distribution-swift.enum/gravityareas.md)
  Stacked views will not have any special distribution behavior, relying on behavior described by gravity areas and set hugging priorities along the stacking axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/distribution-swift.enum/fillproportionally)*