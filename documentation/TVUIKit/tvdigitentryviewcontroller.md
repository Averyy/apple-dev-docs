# TVDigitEntryViewController

**Framework**: TVUIKit  
**Kind**: class

A view controller that enables the user to enter digits, like a passcode, in your app.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
class TVDigitEntryViewController
```

#### Overview

Use the `TVDigitEntryViewController` class to manage a digit entry view. The digit entry view is automatically presented by the view controller and consists of boxes that display digits and a digit keyboard.

![A fullscreen image with five grey boxes in the middle of the screen and a row of numbers from 1 to 0 below the boxes.](/images/com.apple.tvuikit/media-3016866@2x.png)

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
- [UIViewController](../uikit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvdigitentryviewcontroller)*