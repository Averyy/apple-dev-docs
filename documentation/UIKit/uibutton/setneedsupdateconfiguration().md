# setNeedsUpdateConfiguration()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Requests the system update the button configuration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func setNeedsUpdateConfiguration()
```

```objc
- (void) setNeedsUpdateConfiguration;
```

#### Discussion

Call this method to make the system call [`updateConfiguration()`](./updateconfiguration%28%29.md). The system calls this method automatically when the button’s state changes. If you call this method multiple times before the system calls [`updateConfiguration()`](./updateconfiguration%28%29.md), the system calls [`updateConfiguration()`](./updateconfiguration%28%29.md) once.

## See Also

### Managing the appearance with a configuration object
- [var configuration: UIButton.Configuration?](./configuration-5rlyb.md)
  The configuration for the button’s appearance.
- [var automaticallyUpdatesConfiguration: Bool](./automaticallyupdatesconfiguration.md)
  A Boolean value that determines whether the button configuration changes when button’s state changes.
- [func updateConfiguration()](./updateconfiguration%28%29.md)
  Updates the button configuration in response to a button state change.
- [var configurationUpdateHandler: UIButton.ConfigurationUpdateHandler?](./configurationupdatehandler-swift.property.md)
  A closure that executes when the button state changes.
- [typealias ConfigurationUpdateHandler](./configurationupdatehandler-swift.typealias.md)
  A closure to update the configuration of a button.
- [configuration](./configuration-7gz60.md)
  The configuration for the button’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/setneedsupdateconfiguration())*