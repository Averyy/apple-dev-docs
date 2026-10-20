# PKShareSecureElementPassViewController

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
class PKShareSecureElementPassViewController
```

```objc
@interface PKShareSecureElementPassViewController : UIViewController
```

## Topics

### Initializers
- [init(secureElementPass: PKSecureElementPass, delegate: (any PKShareSecureElementPassViewControllerDelegate)?)](./pksharesecureelementpassviewcontroller/init%28secureelementpass,delegate%29.md)
### Instance Properties
- [var delegate: (any PKShareSecureElementPassViewControllerDelegate)?](./pksharesecureelementpassviewcontroller/delegate.md)
- [var promptToShareURL: Bool](./pksharesecureelementpassviewcontroller/prompttoshareurl.md)

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
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### General purpose passes
- [class PKSecureElementPass](./pksecureelementpass.md)
  A pass with a credential that the device stores in a certified payment information chip.
- [class PKAddSecureElementPassConfiguration](./pkaddsecureelementpassconfiguration.md)
  An object that describes the configuration of a secure element payment pass.
- [class PKAddSecureElementPassViewController](./pkaddsecureelementpassviewcontroller.md)
  A view controller that manages the addition of secure element payment passes.
- [class PKPass](./pkpass.md)
  An object that represents a single pass.
- [class PKAddPassesViewController](./pkaddpassesviewcontroller.md)
  Lets your app show a pass and prompt the user to add that pass to the pass library.
- [struct AsyncShareablePassConfiguration](./asyncshareablepassconfiguration.md)
- [protocol PKShareSecureElementPassViewControllerDelegate](./pksharesecureelementpassviewcontrollerdelegate.md)
- [PKShareablePassMetadata.Preview](./pkshareablepassmetadata/preview-swift.class.md)
- [enum PKShareSecureElementPassResult](./pksharesecureelementpassresult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksharesecureelementpassviewcontroller)*