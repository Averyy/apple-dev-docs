# PKAddPassesViewController

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

Lets your app show a pass and prompt the user to add that pass to the pass library.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class PKAddPassesViewController
```

#### Overview

To add multiple passes without presenting this view controller multiple times, use the [`addPasses(_:withCompletionHandler:)`](pkpasslibrary/addpasses(_:withcompletionhandler:).md) method of [`PKPassLibrary`](pkpasslibrary.md).

## Topics

### Determining if the device supports adding passes
- [class func canAddPasses() -> Bool](pkaddpassesviewcontroller/canaddpasses.md)
  Returns a Boolean value that indicates whether the device supports adding passes.
### Creating an add-passes view controller
- [init?(pass: PKPass)](pkaddpassesviewcontroller/init(pass:).md)
  Initializes and returns a newly created add-passes view controller with a single pass.
- [init?(passes: [PKPass])](pkaddpassesviewcontroller/init(passes:).md)
  Initializes and returns a newly created add-passes view controller with an array of passes.
- [init(issuerData: Data, signature: Data) throws](pkaddpassesviewcontroller/init(issuerdata:signature:).md)
  Initializes and returns a new add-passes view controller with the issuer data, and signature you provide.
### Adding passes
- [var delegate: (any PKAddPassesViewControllerDelegate)?](pkaddpassesviewcontroller/delegate.md)
  The view controller’s delegate.
- [protocol PKAddPassesViewControllerDelegate](pkaddpassesviewcontrollerdelegate.md)
  Methods that an add-passes view controller’s delegate implements.

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
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [class PKSecureElementPass](pksecureelementpass.md)
  A pass with a credential that the device stores in a certified payment information chip.
- [class PKAddSecureElementPassConfiguration](pkaddsecureelementpassconfiguration.md)
  An object that describes the configuration of a secure element payment pass.
- [class PKAddSecureElementPassViewController](pkaddsecureelementpassviewcontroller.md)
  A view controller that manages the addition of secure element payment passes.
- [class PKPass](pkpass.md)
  An object that represents a single pass.
- [struct AsyncShareablePassConfiguration](asyncshareablepassconfiguration.md)
- [class PKShareSecureElementPassViewController](pksharesecureelementpassviewcontroller.md)
- [protocol PKShareSecureElementPassViewControllerDelegate](pksharesecureelementpassviewcontrollerdelegate.md)
- [PKShareablePassMetadata.Preview](pkshareablepassmetadata/preview-swift.class.md)
- [enum PKShareSecureElementPassResult](pksharesecureelementpassresult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller)*