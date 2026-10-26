# configuration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The configuration for the button’s appearance.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, copy, readwrite, nullable) UIButtonConfiguration * configuration;
```

#### Discussion

Setting a configuration opts the button into a configuration system based on [`UIButtonConfiguration`](../uibuttonconfiguration.md). This configuration supports several options and behaviors unavailable with other configuration methods. Features include subtitle labels, extended control over background appearance, ways to transform the button configuration when the button changes state, and integration with macOS when building with Mac Catalyst.

When using a configuration, the button ignores deprecated methods and properties of [`UIButton`](../uibutton.md). You can combine most other methods and properties of [`UIButton`](../uibutton.md) with a configuration. If you have existing code to configure a button, you can set this property to take advantage of additional configuration features.

If the configuration is `nil`, other supported properties and methods of [`UIButton`](../uibutton.md), such as [`setTitle(_:for:)`](./settitle%28_,for%29.md) , control the appearance of the button.

## See Also

### Managing the appearance with a configuration object
- [var automaticallyUpdatesConfiguration: Bool](./automaticallyupdatesconfiguration.md)
  A Boolean value that determines whether the button configuration changes when button’s state changes.
- [func setNeedsUpdateConfiguration()](./setneedsupdateconfiguration%28%29.md)
  Requests the system update the button configuration.
- [func updateConfiguration()](./updateconfiguration%28%29.md)
  Updates the button configuration in response to a button state change.
- [var configurationUpdateHandler: UIButton.ConfigurationUpdateHandler?](./configurationupdatehandler-swift.property.md)
  A closure that executes when the button state changes.
- [typealias ConfigurationUpdateHandler](./configurationupdatehandler-swift.typealias.md)
  A closure to update the configuration of a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-7gz60)*