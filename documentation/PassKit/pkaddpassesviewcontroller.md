# PKAddPassesViewController

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

Lets your app show a pass and prompt the user to add that pass to the pass library.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class PKAddPassesViewController
```

```objc
@interface PKAddPassesViewController : UIViewController
```

#### Overview

To add multiple passes without presenting this view controller multiple times, use the [`addPasses(_:withCompletionHandler:)`](./pkpasslibrary/addpasses%28_,withcompletionhandler%29.md) method of [`PKPassLibrary`](./pkpasslibrary.md).

## Topics

### Determining if the device supports adding passes
- [class func canAddPasses() -> Bool](./pkaddpassesviewcontroller/canaddpasses%28%29.md)
  Returns a Boolean value that indicates whether the device supports adding passes.
### Creating an add-passes view controller
- [init?(pass: PKPass)](./pkaddpassesviewcontroller/init%28pass%29.md)
  Initializes and returns a newly created add-passes view controller with a single pass.
- [init?(passes: [PKPass])](./pkaddpassesviewcontroller/init%28passes%29.md)
  Initializes and returns a newly created add-passes view controller with an array of passes.
- [init(issuerData: Data, signature: Data) throws](./pkaddpassesviewcontroller/init%28issuerdata,signature%29.md)
  Initializes and returns a new add-passes view controller with the issuer data, and signature you provide.
### Adding passes
- [var delegate: (any PKAddPassesViewControllerDelegate)?](./pkaddpassesviewcontroller/delegate.md)
  The view controller’s delegate.
- [protocol PKAddPassesViewControllerDelegate](./pkaddpassesviewcontrollerdelegate.md)
  Methods that an add-passes view controller’s delegate implements.
### Initializers
- [init?(passesArchiveAt: URL)](./pkaddpassesviewcontroller/init%28passesarchiveat%29.md)
- [init?(passesArchiveAtFileURL: URL)](./pkaddpassesviewcontroller/init%28passesarchiveatfileurl%29.md)
- [init?(passesArchiveData: Data)](./pkaddpassesviewcontroller/init%28passesarchivedata%29.md)
- [init?(passesData: [Data])](./pkaddpassesviewcontroller/init%28passesdata%29.md)

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
- [struct AsyncShareablePassConfiguration](./asyncshareablepassconfiguration.md)
- [class PKShareSecureElementPassViewController](./pksharesecureelementpassviewcontroller.md)
- [protocol PKShareSecureElementPassViewControllerDelegate](./pksharesecureelementpassviewcontrollerdelegate.md)
- [PKShareablePassMetadata.Preview](./pkshareablepassmetadata/preview-swift.class.md)
- [enum PKShareSecureElementPassResult](./pksharesecureelementpassresult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller)*