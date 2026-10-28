# indirectPointerTouchModes

**Framework**: PaperKit  
**Kind**: property  
**Role**: Instance Property

The modes available for a user to select.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency var indirectPointerTouchModes: [PaperMarkupViewController.TouchMode] { get set }
```

## Discussion

Default is `[.selection, .drawing]`

## See Also

### Managing touch modes
- [var selectedIndirectPointerTouchMode: PaperMarkupViewController.TouchMode](./selectedindirectpointertouchmode.md)
  The currently selected pointer mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuptoolbarviewcontroller/indirectpointertouchmodes)*