# FPUIActionExtensionViewController

**Framework**: File Provider UI  
**Kind**: class

The custom user interface used to perform a selected action.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class FPUIActionExtensionViewController
```

## Mentions

- [Adding Actions to the Context Menu](adding-actions-to-the-context-menu.md)

#### Overview

Subclass this view controller to provide the user interface for your actions.

No matter how many actions you define, your File Provider UI extension has only one `FPUIActionExtensionViewController` subclass. When the user selects one of your actions, the system instantiates a copy of your subclass, calls its [`prepare(forAction:itemIdentifiers:)`](fpuiactionextensionviewcontroller/prepare(foraction:itemidentifiers:).md) method, and presents it to the user.

Your subclass must do the following:

- Override the [`prepare(forAction:itemIdentifiers:)`](fpuiactionextensionviewcontroller/prepare(foraction:itemidentifiers:).md) method to check the action identifiers and present an appropriate user interface for the selected actions.
- Provide some sort of feedback, even if the action doesn’t require interaction with the user. For example, present a view that quickly fades out and automatically completes the action.
- Call the [`extensionContext`](fpuiactionextensionviewcontroller/extensioncontext.md) object’s [`cancelRequest(withError:)`](fpuiactionextensioncontext/cancelrequest(witherror:).md) or [`completeRequest()`](fpuiactionextensioncontext/completerequest().md) method when the action is finished to complete the action.

## Topics

### Working with Actions
- [func prepare(forAction: String, itemIdentifiers: [NSFileProviderItemIdentifier])](fpuiactionextensionviewcontroller/prepare(foraction:itemidentifiers:).md)
  Performs any necessary setup or configuration for the specified action.
- [func prepare(forError: any Error)](fpuiactionextensionviewcontroller/prepare(forerror:).md)
  Performs any necessary setup or configuration when an authentication error occurs.
- [var extensionContext: FPUIActionExtensionContext](fpuiactionextensionviewcontroller/extensioncontext.md)
  The extension context provided by the host app.
- [class FPUIActionExtensionContext](fpuiactionextensioncontext.md)
  An extension context provided to File Provider UI extensions.

## Relationships

### Inherits From
- [NSViewController](../appkit/nsviewcontroller.md)
- [UIViewController](../uikit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSEditor](../appkit/nseditor.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSeguePerforming](../appkit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [Adding Actions to the Context Menu](adding-actions-to-the-context-menu.md)
  Present custom actions from your File Provider extension in the system’s file browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileproviderui/fpuiactionextensionviewcontroller)*