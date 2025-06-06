# automaticallyUpdatesConfiguration

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the button configuration changes when button’s state changes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var automaticallyUpdatesConfiguration: Bool { get set }
```

#### Discussion

Set this property to [`true`](https://developer.apple.com/documentation/swift/true) to have the button call [`updated(for:)`](uibutton/configuration-swift.struct/updated(for:).md) (Swift) or [`updatedConfigurationForButton:`](uibuttonconfiguration/updatedconfigurationforbutton:.md) (Objective-C) when the button state changes and apply the changes to the button. The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var configuration: UIButton.Configuration?](uibutton/configuration-5rlyb.md)
  The configuration for the button’s appearance.
- [func setNeedsUpdateConfiguration()](uibutton/setneedsupdateconfiguration.md)
  Requests the system update the button configuration.
- [func updateConfiguration()](uibutton/updateconfiguration.md)
  Updates the button configuration in response to a button state change.
- [var configurationUpdateHandler: UIButton.ConfigurationUpdateHandler?](uibutton/configurationupdatehandler-swift.property.md)
  A closure that executes when the button state changes.
- [typealias ConfigurationUpdateHandler](uibutton/configurationupdatehandler-swift.typealias.md)
  A closure to update the configuration of a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/automaticallyupdatesconfiguration)*