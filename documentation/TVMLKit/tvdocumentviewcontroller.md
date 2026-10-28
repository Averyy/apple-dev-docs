# TVDocumentViewController

**Framework**: TVMLKit  
**Kind**: class  
**Role**: Class

A view controller that represents a TVMLKit document.

**Availability**:
- tvOS 13.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
class TVDocumentViewController
```

```objc
@interface TVDocumentViewController : UIViewController
```

## Overview

Instances of this class serve as bridges into `TVMLKit JS`’s document life cycle, and allow for native event handling with `TVMLKit`. This class also provides a way for native clients to communicate with `TVMLKit JS`.

## Topics

### Initializing the Document View Controller
- [convenience init(context: [String : Any], for: TVApplicationController)](./tvdocumentviewcontroller/init%28context,for%29.md)
  Creates a new document view controller with a specific context and app controller.
### Managing Interactions with the Document
- [var delegate: (any TVDocumentViewControllerDelegate)?](./tvdocumentviewcontroller/delegate.md)
  The delegate for handling events in the document view controller.
- [protocol TVDocumentViewControllerDelegate](./tvdocumentviewcontrollerdelegate.md)
  Methods to manage updates, events, and errors from the document view controller.
### Handling Document Events
- [TVDocumentViewController.Event](./tvdocumentviewcontroller/event.md)
  Events that can be triggered on the document view controller.
### Updating the Document View Controller
- [func update(using: [String : Any])](./tvdocumentviewcontroller/update%28using%29.md)
  Updates the document view controller with the provided context.
### Accessing the Document’s Components
- [var appController: TVApplicationController?](./tvdocumentviewcontroller/appcontroller.md)
  The document’s app controller that bridges UI, navigation stack, storage, and event handling from JavaScript.
- [var documentContext: [String : Any]](./tvdocumentviewcontroller/documentcontext.md)
  The current document context.
### Instance Methods
- [- init](./tvdocumentviewcontroller/init.md)
- [- initWithCoder:](./tvdocumentviewcontroller/initwithcoder_.md)
- [- initWithNibName:bundle:](./tvdocumentviewcontroller/initwithnibname_bundle_.md)

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
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Views and View Controllers
- [class TVViewElement](./tvviewelement.md)
  A representation of a read-only DOM node.
- [protocol TVInterfaceCreating](./tvinterfacecreating.md)
  A protocol that defines methods used to create views and view controllers.
- [class TVInterfaceFactory](./tvinterfacefactory.md)
  A factory for the creation of views and view controllers.
- [class TVBrowserViewController](./tvbrowserviewcontroller.md)
  A view controller that presents content in a browsable, full-screen format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvdocumentviewcontroller)*