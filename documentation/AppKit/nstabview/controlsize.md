# controlSize

**Framework**: AppKit  
**Kind**: property

The size of the tab view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var controlSize: NSControl.ControlSize { get set }
```

#### Discussion

The valid values for this property are described inControl Sizes in [`NSCell`](nscell.md). The default value of this property is [`NSRegularControlSize`](nsregularcontrolsize.md).

## See Also

- [var minimumSize: NSSize](nstabview/minimumsize.md)
  The minimum size necessary for the tab view to display tabs in a useful way.
- [var contentRect: NSRect](nstabview/contentrect.md)
  The rectangle describing the content area of the tab view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/controlsize)*