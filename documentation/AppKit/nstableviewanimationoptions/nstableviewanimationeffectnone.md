# NSTableViewAnimationEffectNone

**Framework**: AppKit  
**Kind**: case  
**Role**: Enumeration Case

Use no animation effects.

**Availability**:
- macOS 10.7+

## Declaration

```c
NSTableViewAnimationEffectNone
```

## See Also

### Constants
- [static var effectFade: NSTableView.AnimationOptions](../nstableview/animationoptions/effectfade.md)
  Use a fade for row or column removal. The effect can be combined with any of the slide constants.
- [static var effectGap: NSTableView.AnimationOptions](../nstableview/animationoptions/effectgap.md)
  Creates a gap for newly inserted rows. This is useful for drag and drop animations that animate to a newly opened gap and should be used in the delegate method [`tableView(_:acceptDrop:row:dropOperation:)`](../nstableviewdatasource/tableview%28_,acceptdrop,row,dropoperation%29.md).
- [static var slideUp: NSTableView.AnimationOptions](../nstableview/animationoptions/slideup.md)
  Animates a row insertion or removal by sliding upward.
- [static var slideDown: NSTableView.AnimationOptions](../nstableview/animationoptions/slidedown.md)
  Animates a row insertion or removal by sliding downward.
- [static var slideLeft: NSTableView.AnimationOptions](../nstableview/animationoptions/slideleft.md)
  Animates a row insertion by sliding from the left. Animates a row removal by sliding towards the left.
- [static var slideRight: NSTableView.AnimationOptions](../nstableview/animationoptions/slideright.md)
  Animates a row insertion by sliding from the right. Animates a row removal by sliding towards the right.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewanimationoptions/nstableviewanimationeffectnone)*