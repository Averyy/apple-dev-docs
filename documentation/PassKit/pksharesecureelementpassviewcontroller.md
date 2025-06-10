# PKShareSecureElementPassViewController

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class PKShareSecureElementPassViewController
```

## Topics

### Initializers
- [init(secureElementPass: PKSecureElementPass, delegate: (any PKShareSecureElementPassViewControllerDelegate)?)](pksharesecureelementpassviewcontroller/init(secureelementpass:delegate:).md)
### Instance Properties
- [var delegate: (any PKShareSecureElementPassViewControllerDelegate)?](pksharesecureelementpassviewcontroller/delegate.md)
- [var promptToShareURL: Bool](pksharesecureelementpassviewcontroller/prompttoshareurl.md)

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
- [SendableMetatype](../Swift/SendableMetatype.md)
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
- [class PKAddPassesViewController](pkaddpassesviewcontroller.md)
  Lets your app show a pass and prompt the user to add that pass to the pass library.
- [struct AsyncShareablePassConfiguration](asyncshareablepassconfiguration.md)
- [protocol PKShareSecureElementPassViewControllerDelegate](pksharesecureelementpassviewcontrollerdelegate.md)
- [PKShareablePassMetadata.Preview](pkshareablepassmetadata/preview-swift.class.md)
- [enum PKShareSecureElementPassResult](pksharesecureelementpassresult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksharesecureelementpassviewcontroller)*