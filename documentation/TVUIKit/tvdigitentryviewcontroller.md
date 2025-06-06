# TVDigitEntryViewController

**Framework**: TVUIKit  
**Kind**: class

A view controller that enables the user to enter digits, like a passcode, in your app.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
@MainActor
class TVDigitEntryViewController
```

#### Overview

Use the `TVDigitEntryViewController` class to manage a digit entry view. The digit entry view is automatically presented by the view controller and consists of boxes that display digits and a digit keyboard.

![A fullscreen image with five grey boxes in the middle of the screen and a row of numbers from 1 to 0 below the boxes.](https://docs-assets.developer.apple.com/published/0f7a5ceac1464ee65ff1cc5ebe7341fb/media-3016866%402x.png)

## Topics

### Configuring the Digit Entry View
- [var numberOfDigits: Int](tvdigitentryviewcontroller/numberofdigits.md)
  The number of required digits.
- [var titleText: String?](tvdigitentryviewcontroller/titletext.md)
  The title of the digit entry view.
- [var promptText: String?](tvdigitentryviewcontroller/prompttext.md)
  A prompt that displays any additional required information.
- [var isSecureDigitEntry: Bool](tvdigitentryviewcontroller/issecuredigitentry.md)
  A Boolean value that indicates whether an entered digit is immediately obscured.
### Entering Information
- [var entryCompletionHandler: (String) -> Void](tvdigitentryviewcontroller/entrycompletionhandler.md)
  A completion handler that cues the app that the user has entered the required number of digits for the digit entry view.
- [func clearEntry(animated: Bool)](tvdigitentryviewcontroller/clearentry(animated:).md)
  Removes all digits from the digit entry view.

## Relationships

### Inherits From
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvdigitentryviewcontroller)*