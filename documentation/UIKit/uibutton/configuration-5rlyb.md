# configuration

**Framework**: UIKit  
**Kind**: property

The configuration for the button’s appearance.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var configuration: UIButton.Configuration? { get set }
```

#### Discussion

Setting a configuration opts the button into a configuration system based on [`UIButton.Configuration`](uibutton/configuration-swift.struct.md). This configuration supports several options and behaviors unavailable with other configuration methods. Features include subtitle labels, extended control over background appearance, ways to transform the button configuration when the button changes state, and integration with macOS when building with Mac Catalyst.

When using a configuration, the button ignores deprecated methods and properties of [`UIButton`](uibutton.md). You can combine most other methods and properties of [`UIButton`](uibutton.md) with a configuration. If you have existing code to configure a button, you can set this property to take advantage of additional configuration features.

If the configuration is `nil`, other supported properties and methods of [`UIButton`](uibutton.md), such as [`setTitle(_:for:)`](uibutton/settitle(_:for:).md) , control the appearance of the button.

## See Also

- [var automaticallyUpdatesConfiguration: Bool](uibutton/automaticallyupdatesconfiguration.md)
  A Boolean value that determines whether the button configuration changes when button’s state changes.
- [func setNeedsUpdateConfiguration()](uibutton/setneedsupdateconfiguration.md)
  Requests the system update the button configuration.
- [func updateConfiguration()](uibutton/updateconfiguration.md)
  Updates the button configuration in response to a button state change.
- [var configurationUpdateHandler: UIButton.ConfigurationUpdateHandler?](uibutton/configurationupdatehandler-swift.property.md)
  A closure that executes when the button state changes.
- [typealias ConfigurationUpdateHandler](uibutton/configurationupdatehandler-swift.typealias.md)
  A closure to update the configuration of a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-5rlyb)*