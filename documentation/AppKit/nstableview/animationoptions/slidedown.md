# slideDown

**Framework**: AppKit  
**Kind**: property

Animates a row insertion or removal by sliding downward.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static var slideDown: NSTableView.AnimationOptions { get }
```

## See Also

- [static var effectFade: NSTableView.AnimationOptions](nstableview/animationoptions/effectfade.md)
  Use a fade for row or column removal. The effect can be combined with any of the slide constants.
- [static var effectGap: NSTableView.AnimationOptions](nstableview/animationoptions/effectgap.md)
  Creates a gap for newly inserted rows. This is useful for drag and drop animations that animate to a newly opened gap and should be used in the delegate method [`tableView(_:acceptDrop:row:dropOperation:)`](nstableviewdatasource/tableview(_:acceptdrop:row:dropoperation:).md).
- [static var slideUp: NSTableView.AnimationOptions](nstableview/animationoptions/slideup.md)
  Animates a row insertion or removal by sliding upward.
- [static var slideLeft: NSTableView.AnimationOptions](nstableview/animationoptions/slideleft.md)
  Animates a row insertion by sliding from the left. Animates a row removal by sliding towards the left.
- [static var slideRight: NSTableView.AnimationOptions](nstableview/animationoptions/slideright.md)
  Animates a row insertion by sliding from the right. Animates a row removal by sliding towards the right.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/animationoptions/slidedown)*