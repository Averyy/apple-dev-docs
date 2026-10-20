# TVDigitEntryViewController

**Framework**: TVUIKit  
**Kind**: class  
**Role**: Class

A view controller that enables the user to enter digits, like a passcode, in your app.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
class TVDigitEntryViewController
```

```objc
@interface TVDigitEntryViewController : UIViewController
```

#### Overview

Use the `TVDigitEntryViewController` class to manage a digit entry view. The digit entry view is automatically presented by the view controller and consists of boxes that display digits and a digit keyboard.

![A fullscreen image with five grey boxes in the middle of the screen and a row of numbers from 1 to 0 below the boxes.](https://developer.apple.com/tutorials/images/com.apple.tvuikit/media-3016866@2x.png)

## Topics

### Configuring the Digit Entry View
- [var numberOfDigits: Int](./tvdigitentryviewcontroller/numberofdigits.md)
  The number of required digits.
- [var titleText: String?](./tvdigitentryviewcontroller/titletext.md)
  The title of the digit entry view.
- [var promptText: String?](./tvdigitentryviewcontroller/prompttext.md)
  A prompt that displays any additional required information.
- [var isSecureDigitEntry: Bool](./tvdigitentryviewcontroller/issecuredigitentry.md)
  A Boolean value that indicates whether an entered digit is immediately obscured.
### Entering Information
- [var entryCompletionHandler: (String) -> Void](./tvdigitentryviewcontroller/entrycompletionhandler.md)
  A completion handler that cues the app that the user has entered the required number of digits for the digit entry view.
- [func clearEntry(animated: Bool)](./tvdigitentryviewcontroller/clearentry%28animated%29.md)
  Removes all digits from the digit entry view.

## Relationships

### Inherits From
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvdigitentryviewcontroller)*