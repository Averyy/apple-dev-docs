# automaticallyUpdatesConfiguration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the button configuration changes when button’s state changes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var automaticallyUpdatesConfiguration: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite) BOOL automaticallyUpdatesConfiguration;
```

#### Discussion

Set this property to [`true`](../../Swift/true.md) to have the button call [`updated(for:)`](./configuration-swift.struct/updated%28for%29.md) (Swift) or [`updatedConfigurationForButton:`](../uibuttonconfiguration/updatedconfigurationforbutton_.md) (Objective-C) when the button state changes and apply the changes to the button. The default value is [`true`](../../Swift/true.md).

## See Also

### Managing the appearance with a configuration object
- [var configuration: UIButton.Configuration?](./configuration-5rlyb.md)
  The configuration for the button’s appearance.
- [func setNeedsUpdateConfiguration()](./setneedsupdateconfiguration%28%29.md)
  Requests the system update the button configuration.
- [func updateConfiguration()](./updateconfiguration%28%29.md)
  Updates the button configuration in response to a button state change.
- [var configurationUpdateHandler: UIButton.ConfigurationUpdateHandler?](./configurationupdatehandler-swift.property.md)
  A closure that executes when the button state changes.
- [typealias ConfigurationUpdateHandler](./configurationupdatehandler-swift.typealias.md)
  A closure to update the configuration of a button.
- [configuration](./configuration-7gz60.md)
  The configuration for the button’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/automaticallyupdatesconfiguration)*