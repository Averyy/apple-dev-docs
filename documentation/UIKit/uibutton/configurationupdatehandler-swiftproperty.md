# configurationUpdateHandler

**Framework**: UIKit  
**Kind**: property

A closure that executes when the button state changes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var configurationUpdateHandler: UIButton.ConfigurationUpdateHandler? { get set }
```

#### Discussion

Use this property as an alternative to overriding [`updateConfiguration()`](uibutton/updateconfiguration().md). Set a closure to respond to button state changes by updating the button configuration.

In iOS 18 and later, UIKit supports automatic trait tracking inside this closure for traits from this button’s `traitCollection`. For more information, see [`Automatic trait tracking`](automatic-trait-tracking.md).

This closure supports automatic observation tracking. For more information, see [`Updating views automatically with observation tracking`](updating-views-automatically-with-observation-tracking.md).

## See Also

- [func updateConfiguration()](uibutton/updateconfiguration.md)
  Updates the button configuration in response to a button state change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configurationupdatehandler-swift.property)*