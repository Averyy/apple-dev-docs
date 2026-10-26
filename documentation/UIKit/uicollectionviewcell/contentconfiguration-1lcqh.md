# contentConfiguration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current content configuration of the cell.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) id<UIContentConfiguration> contentConfiguration;
```

#### Discussion

Using a content configuration, you can set the cell’s content and styling for a variety of different cell states.

Setting a content configuration replaces the existing [`contentView`](./contentview.md) of the cell with a new content view instance from the configuration, or directly applies the configuration to the existing content view if the configuration is compatible with the existing content view type.

The default value is `nil`. After you set a content configuration to this property, setting this property back to `nil` replaces the current content view with a new, empty content view.

## See Also

### Managing the content
- [var automaticallyUpdatesContentConfiguration: Bool](./automaticallyupdatescontentconfiguration.md)
  A Boolean value that determines whether the cell automatically updates its content configuration when its state changes.
- [var contentView: UIView](./contentview.md)
  The main view that you add your cell’s custom content to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcell/contentconfiguration-1lcqh)*