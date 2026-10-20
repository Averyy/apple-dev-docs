# effectGap

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Creates a gap for newly inserted rows. This is useful for drag and drop animations that animate to a newly opened gap and should be used in the delegate method [`tableView(_:acceptDrop:row:dropOperation:)`](../../nstableviewdatasource/tableview%28_,acceptdrop,row,dropoperation%29.md).

**Availability**:
- macOS 10.7+

## Declaration

```swift
static var effectGap: NSTableView.AnimationOptions { get }
```

```c
NSTableViewAnimationEffectGap
```

## See Also

### Constants
- [static var effectFade: NSTableView.AnimationOptions](./effectfade.md)
  Use a fade for row or column removal. The effect can be combined with any of the slide constants.
- [static var slideUp: NSTableView.AnimationOptions](./slideup.md)
  Animates a row insertion or removal by sliding upward.
- [static var slideDown: NSTableView.AnimationOptions](./slidedown.md)
  Animates a row insertion or removal by sliding downward.
- [static var slideLeft: NSTableView.AnimationOptions](./slideleft.md)
  Animates a row insertion by sliding from the left. Animates a row removal by sliding towards the left.
- [static var slideRight: NSTableView.AnimationOptions](./slideright.md)
  Animates a row insertion by sliding from the right. Animates a row removal by sliding towards the right.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/animationoptions/effectgap)*