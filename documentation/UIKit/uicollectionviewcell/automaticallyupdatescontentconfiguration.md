# automaticallyUpdatesContentConfiguration

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the cell automatically updates its content configuration when its state changes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var automaticallyUpdatesContentConfiguration: Bool { get set }
```

#### Discussion

When this value is [`true`](https://developer.apple.com/documentation/Swift/true), the cell automatically calls [`updated(for:)`](uicontentconfiguration-9eib5/updated(for:).md) on its [`contentConfiguration`](uicollectionviewcell/contentconfiguration-1lcqh.md) when the cell’s [`configurationState`](uicollectionviewcell/configurationstate-4269k.md) changes, and applies the updated configuration back to the cell. The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

If you override [`updateConfiguration(using:)`](uicollectionviewcell/updateconfiguration(using:).md) to manually update and customize the content configuration, disable automatic updates by setting this property to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var contentConfiguration: (any UIContentConfiguration)?](uicollectionviewcell/contentconfiguration-13e7k.md)
  The current content configuration of the cell.
- [var contentView: UIView](uicollectionviewcell/contentview.md)
  The main view that you add your cell’s custom content to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcell/automaticallyupdatescontentconfiguration)*