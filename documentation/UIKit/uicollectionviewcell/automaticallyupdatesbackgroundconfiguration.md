# automaticallyUpdatesBackgroundConfiguration

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var automaticallyUpdatesBackgroundConfiguration: Bool { get set }
```

#### Discussion

When this value is [`true`](https://developer.apple.com/documentation/Swift/true), the cell automatically calls `updated(for:)` on its [`backgroundConfiguration`](uicollectionviewcell/backgroundconfiguration-39dc0.md) when the cell’s [`configurationState`](uicollectionviewcell/configurationstate-4269k.md) changes, and applies the updated configuration back to the cell. The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

If you override [`updateConfiguration(using:)`](uicollectionviewcell/updateconfiguration(using:).md) to manually update and customize the background configuration, disable automatic updates by setting this property to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func defaultBackgroundConfiguration() -> UIBackgroundConfiguration](uicollectionviewcell/defaultbackgroundconfiguration.md)
  Retrieves a background configuration with system default values.
- [var backgroundConfiguration: UIBackgroundConfiguration?](uicollectionviewcell/backgroundconfiguration-rgj4.md)
  The current background configuration of the cell.
- [var backgroundView: UIView?](uicollectionviewcell/backgroundview.md)
  The view that displays behind the cell’s other content.
- [var selectedBackgroundView: UIView?](uicollectionviewcell/selectedbackgroundview.md)
  The view that displays just above the background view for a selected cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcell/automaticallyupdatesbackgroundconfiguration)*