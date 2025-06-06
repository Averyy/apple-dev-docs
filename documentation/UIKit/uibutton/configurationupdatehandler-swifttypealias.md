# UIButton.ConfigurationUpdateHandler

**Framework**: UIKit  
**Kind**: typealias

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

## Parameters

- `button`: The button to update.

## See Also

- [var configuration: UIButton.Configuration?](uibutton/configuration-5rlyb.md)
  The configuration for the button’s appearance.
- [var automaticallyUpdatesConfiguration: Bool](uibutton/automaticallyupdatesconfiguration.md)
  A Boolean value that determines whether the button configuration changes when button’s state changes.
- [func setNeedsUpdateConfiguration()](uibutton/setneedsupdateconfiguration.md)
  Requests the system update the button configuration.
- [func updateConfiguration()](uibutton/updateconfiguration.md)
  Updates the button configuration in response to a button state change.
- [var configurationUpdateHandler: UIButton.ConfigurationUpdateHandler?](uibutton/configurationupdatehandler-swift.property.md)
  A closure that executes when the button state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configurationupdatehandler-swift.typealias)*