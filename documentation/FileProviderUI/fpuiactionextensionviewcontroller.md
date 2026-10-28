# FPUIActionExtensionViewController

**Framework**: File Provider UI  
**Kind**: class  
**Role**: Class

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

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
@interface FPUIActionExtensionViewController : UIViewController
```

*macOS*

```objc
@interface FPUIActionExtensionViewController : NSViewController
```

## Mentions

- [Adding Actions to the Context Menu](./adding-actions-to-the-context-menu.md)

## Overview

Subclass this view controller to provide the user interface for your actions.

No matter how many actions you define, your File Provider UI extension has only one `FPUIActionExtensionViewController` subclass. When the user selects one of your actions, the system instantiates a copy of your subclass, calls its [`prepare(forAction:itemIdentifiers:)`](./fpuiactionextensionviewcontroller/prepare%28foraction,itemidentifiers%29.md) method, and presents it to the user.

Your subclass must do the following:

- Override the [`prepare(forAction:itemIdentifiers:)`](./fpuiactionextensionviewcontroller/prepare%28foraction,itemidentifiers%29.md) method to check the action identifiers and present an appropriate user interface for the selected actions.
- Provide some sort of feedback, even if the action doesn’t require interaction with the user. For example, present a view that quickly fades out and automatically completes the action.
- Call the [`extensionContext`](./fpuiactionextensionviewcontroller/extensioncontext.md) object’s [`cancelRequest(withError:)`](./fpuiactionextensioncontext/cancelrequest%28witherror%29.md) or [`completeRequest()`](./fpuiactionextensioncontext/completerequest%28%29.md) method when the action is finished to complete the action.

## Topics

### Working with Actions
- [func prepare(forAction: String, itemIdentifiers: [NSFileProviderItemIdentifier])](./fpuiactionextensionviewcontroller/prepare%28foraction,itemidentifiers%29.md)
  Performs any necessary setup or configuration for the specified action.
- [func prepare(forError: any Error)](./fpuiactionextensionviewcontroller/prepare%28forerror%29.md)
  Performs any necessary setup or configuration when an authentication error occurs.
- [var extensionContext: FPUIActionExtensionContext](./fpuiactionextensionviewcontroller/extensioncontext.md)
  The extension context provided by the host app.
- [class FPUIActionExtensionContext](./fpuiactionextensioncontext.md)
  An extension context provided to File Provider UI extensions.

## Relationships

### Inherits From
- [NSViewController](../AppKit/nsviewcontroller.md)
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSEditor](../AppKit/nseditor.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSeguePerforming](../AppKit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
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

### Document Browser Customization
- [Adding Actions to the Context Menu](./adding-actions-to-the-context-menu.md)
  Present custom actions from your File Provider extension in the system’s file browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileproviderui/fpuiactionextensionviewcontroller)*