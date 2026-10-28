# updateConfiguration()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Updates the button configuration in response to a button state change.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func updateConfiguration()
```

```objc
- (void) updateConfiguration;
```

## Discussion

Override this method in your subclass to respond changes to the button’s state. Make any necessary changes and update the button’s configuration.

Don’t call this method directly. Call [`setNeedsUpdateConfiguration()`](./setneedsupdateconfiguration%28%29.md) to request an update to your button.

In iOS 18 and later, UIKit supports automatic trait tracking inside this method for traits from this button’s `traitCollection`. For more information, see [Automatic trait tracking](../automatic-trait-tracking.md).

This method supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md).

## See Also

### Observing data in buttons
- [var configurationUpdateHandler: UIButton.ConfigurationUpdateHandler?](./configurationupdatehandler-swift.property.md)
  A closure that executes when the button state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/updateconfiguration())*