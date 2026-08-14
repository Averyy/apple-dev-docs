# TVDocumentViewController

**Framework**: TVMLKit  
**Kind**: class

A view controller that represents a TVMLKit document.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
class TVDocumentViewController
```

#### Overview

Instances of this class serve as bridges into `TVMLKit JS`’s document life cycle, and allow for native event handling with `TVMLKit`. This class also provides a way for native clients to communicate with `TVMLKit JS`.

## Topics

### Initializing the Document View Controller
- [convenience init(context: [String : Any], for: TVApplicationController)](tvdocumentviewcontroller/init(context:for:).md)
  Creates a new document view controller with a specific context and app controller.
### Managing Interactions with the Document
- [var delegate: (any TVDocumentViewControllerDelegate)?](tvdocumentviewcontroller/delegate.md)
  The delegate for handling events in the document view controller.
- [protocol TVDocumentViewControllerDelegate](tvdocumentviewcontrollerdelegate.md)
  Methods to manage updates, events, and errors from the document view controller.
### Handling Document Events
- [TVDocumentViewController.Event](tvdocumentviewcontroller/event.md)
  Events that can be triggered on the document view controller.
### Updating the Document View Controller
- [func update(using: [String : Any])](tvdocumentviewcontroller/update(using:).md)
  Updates the document view controller with the provided context.
### Accessing the Document’s Components
- [var appController: TVApplicationController?](tvdocumentviewcontroller/appcontroller.md)
  The document’s app controller that bridges UI, navigation stack, storage, and event handling from JavaScript.
- [var documentContext: [String : Any]](tvdocumentviewcontroller/documentcontext.md)
  The current document context.

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
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [class TVViewElement](tvviewelement.md)
  A representation of a read-only DOM node.
- [protocol TVInterfaceCreating](tvinterfacecreating.md)
  A protocol that defines methods used to create views and view controllers.
- [class TVInterfaceFactory](tvinterfacefactory.md)
  A factory for the creation of views and view controllers.
- [class TVBrowserViewController](tvbrowserviewcontroller.md)
  A view controller that presents content in a browsable, full-screen format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvdocumentviewcontroller)*