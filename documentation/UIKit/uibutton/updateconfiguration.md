# updateConfiguration()

**Framework**: UIKit  
**Kind**: method

Updates the button configuration in response to a button state change.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func updateConfiguration()
```

#### Discussion

Override this method in your subclass to respond changes to the button’s state. Make any necessary changes and update the button’s configuration.

Don’t call this method directly. Call [`setNeedsUpdateConfiguration()`](uibutton/setneedsupdateconfiguration().md) to request an update to your button.

In iOS 18 and later, UIKit supports automatic trait tracking inside this method for traits from this button’s `traitCollection`. For more information, see [`Automatic trait tracking`](automatic-trait-tracking.md).

This method supports automatic observation tracking. For more information, see [`Updating views automatically with observation tracking`](updating-views-automatically-with-observation-tracking.md).

## See Also

- [var configurationUpdateHandler: UIButton.ConfigurationUpdateHandler?](uibutton/configurationupdatehandler-swift.property.md)
  A closure that executes when the button state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/updateconfiguration())*