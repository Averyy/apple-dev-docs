# backgroundConfiguration

**Framework**: UIKit  
**Kind**: property

The current background configuration of the cell.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var backgroundConfiguration: UIBackgroundConfiguration? { get set }
```

#### Discussion

Using a background configuration, you can obtain system default background styling for a variety of different cell states. Create a background configuration with one of the default system styles, customize the configuration to match your cell’s style as necessary, and assign the configuration to this property.

```swift
var backgroundConfig = UIBackgroundConfiguration.listPlainCell()

// Set a nil background color to use the view's tint color. 
backgroundConfig.backgroundColor = nil 

cell.backgroundConfiguration = backgroundConfig 
```

A background configuration is mutually exclusive with background views, so you must use one approach or the other. Setting a non-`nil` value for this property resets the following APIs to `nil`:

- [`backgroundColor`](uiview/backgroundcolor.md)
- [`backgroundView`](uicollectionviewcell/backgroundview.md)
- [`selectedBackgroundView`](uicollectionviewcell/selectedbackgroundview.md)

## See Also

- [func defaultBackgroundConfiguration() -> UIBackgroundConfiguration](uicollectionviewcell/defaultbackgroundconfiguration.md)
  Retrieves a background configuration with system default values.
- [var automaticallyUpdatesBackgroundConfiguration: Bool](uicollectionviewcell/automaticallyupdatesbackgroundconfiguration.md)
  A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.
- [var backgroundView: UIView?](uicollectionviewcell/backgroundview.md)
  The view that displays behind the cell’s other content.
- [var selectedBackgroundView: UIView?](uicollectionviewcell/selectedbackgroundview.md)
  The view that displays just above the background view for a selected cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcell/backgroundconfiguration-rgj4)*