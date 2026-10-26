# automaticallyUpdatesContentConfiguration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the cell automatically updates its content configuration when its state changes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var automaticallyUpdatesContentConfiguration: Bool { get set }
```

```objc
@property (nonatomic) BOOL automaticallyUpdatesContentConfiguration;
```

#### Discussion

When this value is [`true`](../../Swift/true.md), the cell automatically calls [`updated(for:)`](../uicontentconfiguration-9eib5/updated%28for%29.md) on its [`contentConfiguration`](./contentconfiguration-1lcqh.md) when the cell’s [`configurationState`](./configurationstate-4269k.md) changes, and applies the updated configuration back to the cell. The default value is [`true`](../../Swift/true.md).

If you override [`updateConfiguration(using:)`](./updateconfiguration%28using%29.md) to manually update and customize the content configuration, disable automatic updates by setting this property to [`false`](../../Swift/false.md).

## See Also

### Managing the content
- [var contentConfiguration: (any UIContentConfiguration)?](./contentconfiguration-13e7k.md)
  The current content configuration of the cell.
- [var contentView: UIView](./contentview.md)
  The main view that you add your cell’s custom content to.
- [contentConfiguration](./contentconfiguration-1lcqh.md)
  The current content configuration of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcell/automaticallyupdatescontentconfiguration)*