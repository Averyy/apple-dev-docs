# UIButton.ConfigurationUpdateHandler

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

A closure to update the configuration of a button.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
typealias ConfigurationUpdateHandler = (UIButton) -> Void
```

```c
typedef void (^)(__kindof UIButton *) UIButtonConfigurationUpdateHandler;
```

## Parameters

- `button`: The button to update.

## See Also

### Managing the appearance with a configuration object
- [var configuration: UIButton.Configuration?](./configuration-5rlyb.md)
  The configuration for the button’s appearance.
- [var automaticallyUpdatesConfiguration: Bool](./automaticallyupdatesconfiguration.md)
  A Boolean value that determines whether the button configuration changes when button’s state changes.
- [func setNeedsUpdateConfiguration()](./setneedsupdateconfiguration%28%29.md)
  Requests the system update the button configuration.
- [func updateConfiguration()](./updateconfiguration%28%29.md)
  Updates the button configuration in response to a button state change.
- [var configurationUpdateHandler: UIButton.ConfigurationUpdateHandler?](./configurationupdatehandler-swift.property.md)
  A closure that executes when the button state changes.
- [configuration](./configuration-7gz60.md)
  The configuration for the button’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configurationupdatehandler-swift.typealias)*