# selectedBackgroundView

**Framework**: UIKit  
**Kind**: property

The view that displays just above the background view for a selected cell.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var selectedBackgroundView: UIView? { get set }
```

#### Discussion

You can use this view to give a selected cell a custom appearance. When the cell has a selected state, this view layers above the [`backgroundView`](uicollectionviewcell/backgroundview.md) and behind the [`contentView`](uicollectionviewcell/contentview.md).

A background configuration is mutually exclusive with background views, so you must use one approach or the other. Setting a non-`nil` value for this property resets [`backgroundConfiguration`](uicollectionviewcell/backgroundconfiguration-rgj4.md) to `nil`.

## See Also

- [func defaultBackgroundConfiguration() -> UIBackgroundConfiguration](uicollectionviewcell/defaultbackgroundconfiguration.md)
  Retrieves a background configuration with system default values.
- [var backgroundConfiguration: UIBackgroundConfiguration?](uicollectionviewcell/backgroundconfiguration-rgj4.md)
  The current background configuration of the cell.
- [var automaticallyUpdatesBackgroundConfiguration: Bool](uicollectionviewcell/automaticallyupdatesbackgroundconfiguration.md)
  A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.
- [var backgroundView: UIView?](uicollectionviewcell/backgroundview.md)
  The view that displays behind the cell’s other content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcell/selectedbackgroundview)*