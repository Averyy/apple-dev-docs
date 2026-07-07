# defaultBackgroundConfiguration

**Framework**: UIKit  
**Kind**: method

Retrieves a background configuration with system default values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
- (UIBackgroundConfiguration *) defaultBackgroundConfiguration;
```

#### Return Value

A default background configuration. The system determines default values for the configuration according to the section where the cell appears.

## See Also

- [backgroundConfiguration](uicollectionviewcell/backgroundconfiguration-39dc0.md)
  The current background configuration of the cell.
- [var automaticallyUpdatesBackgroundConfiguration: Bool](uicollectionviewcell/automaticallyupdatesbackgroundconfiguration.md)
  A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.
- [var backgroundView: UIView?](uicollectionviewcell/backgroundview.md)
  The view that displays behind the cell’s other content.
- [var selectedBackgroundView: UIView?](uicollectionviewcell/selectedbackgroundview.md)
  The view that displays just above the background view for a selected cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcell/defaultbackgroundconfiguration)*