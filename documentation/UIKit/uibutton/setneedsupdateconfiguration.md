# setNeedsUpdateConfiguration()

**Framework**: UIKit  
**Kind**: method

Requests the system update the button configuration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setNeedsUpdateConfiguration()
```

#### Discussion

Call this method to make the system call [`updateConfiguration()`](uibutton/updateconfiguration().md). The system calls this method automatically when the button’s state changes. If you call this method multiple times before the system calls [`updateConfiguration()`](uibutton/updateconfiguration().md), the system calls [`updateConfiguration()`](uibutton/updateconfiguration().md) once.

## See Also

- [var configuration: UIButton.Configuration?](uibutton/configuration-5rlyb.md)
  The configuration for the button’s appearance.
- [var automaticallyUpdatesConfiguration: Bool](uibutton/automaticallyupdatesconfiguration.md)
  A Boolean value that determines whether the button configuration changes when button’s state changes.
- [func updateConfiguration()](uibutton/updateconfiguration.md)
  Updates the button configuration in response to a button state change.
- [var configurationUpdateHandler: UIButton.ConfigurationUpdateHandler?](uibutton/configurationupdatehandler-swift.property.md)
  A closure that executes when the button state changes.
- [typealias ConfigurationUpdateHandler](uibutton/configurationupdatehandler-swift.typealias.md)
  A closure to update the configuration of a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/setneedsupdateconfiguration())*