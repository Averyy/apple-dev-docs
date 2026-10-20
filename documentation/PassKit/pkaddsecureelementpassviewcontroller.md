# PKAddSecureElementPassViewController

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

A view controller that manages the addition of secure element payment passes.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
class PKAddSecureElementPassViewController
```

```objc
@interface PKAddSecureElementPassViewController : UIViewController
```

## Topics

### Creating a view controller
- [init?(configuration: PKAddSecureElementPassConfiguration, delegate: (any PKAddSecureElementPassViewControllerDelegate)?)](./pkaddsecureelementpassviewcontroller/init%28configuration,delegate%29.md)
  Creates a view controller using the specified pass configuration.
### Responding to the life cycle of a pass
- [var delegate: (any PKAddSecureElementPassViewControllerDelegate)?](./pkaddsecureelementpassviewcontroller/delegate.md)
  An object that acts as the view controller’s delegate.
- [protocol PKAddSecureElementPassViewControllerDelegate](./pkaddsecureelementpassviewcontrollerdelegate.md)
  The methods for responding to the life cycle events of a Secure Element pass.
### Validating pass configuration
- [class func canAddSecureElementPass(configuration: PKAddSecureElementPassConfiguration) -> Bool](./pkaddsecureelementpassviewcontroller/canaddsecureelementpass%28configuration%29.md)
  Returns a Boolean value that indicates whether PassKit can create a Secure Element pass using the specified configuration.

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
- [class PKPass](./pkpass.md)
  An object that represents a single pass.
- [class PKAddPassesViewController](./pkaddpassesviewcontroller.md)
  Lets your app show a pass and prompt the user to add that pass to the pass library.
- [struct AsyncShareablePassConfiguration](./asyncshareablepassconfiguration.md)
- [class PKShareSecureElementPassViewController](./pksharesecureelementpassviewcontroller.md)
- [protocol PKShareSecureElementPassViewControllerDelegate](./pksharesecureelementpassviewcontrollerdelegate.md)
- [PKShareablePassMetadata.Preview](./pkshareablepassmetadata/preview-swift.class.md)
- [enum PKShareSecureElementPassResult](./pksharesecureelementpassresult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddsecureelementpassviewcontroller)*