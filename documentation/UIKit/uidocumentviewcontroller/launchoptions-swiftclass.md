# UIDocumentViewController.LaunchOptions

**Framework**: UIKit  
**Kind**: class

Options for customizing the document launch view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
class LaunchOptions
```

## Mentions

- [Customizing a document-based app’s launch experience](customizing-a-document-based-app-s-launch-experience.md)

#### Overview

When your app launches, the document view controller displays a view that contains a title and buttons to create new documents. It also displays the document browser as a sheet over the title view. For more information, see [`Customizing a document-based app’s launch experience`](customizing-a-document-based-app-s-launch-experience.md).

## Topics

### Configuring the appearance
- [var title: String](uidocumentviewcontroller/launchoptions-swift.class/title.md)
  The title that appears in the title view.
- [var background: UIBackgroundConfiguration](uidocumentviewcontroller/launchoptions-swift.class/background.md)
  A configuration that describes the launch scene’s background.
- [var documentTargetView: UIView?](uidocumentviewcontroller/launchoptions-swift.class/documenttargetview.md)
  The document target view.
- [var browserViewController: UIDocumentBrowserViewController](uidocumentviewcontroller/launchoptions-swift.class/browserviewcontroller.md)
  The document browser view controller.
### Adding accessory views
- [var backgroundAccessoryView: UIView?](uidocumentviewcontroller/launchoptions-swift.class/backgroundaccessoryview.md)
  A view that appears behind the title view in the launch scene.
- [var foregroundAccessoryView: UIView?](uidocumentviewcontroller/launchoptions-swift.class/foregroundaccessoryview.md)
  A view that appears in front of the title view in the launch scene.
### Adding actions
- [var primaryAction: UIAction?](uidocumentviewcontroller/launchoptions-swift.class/primaryaction.md)
  The launch scene’s primary action.
- [var secondaryAction: UIAction?](uidocumentviewcontroller/launchoptions-swift.class/secondaryaction.md)
  The launch scene’s secondary action.
### Creating documents
- [class func createDocumentAction(withIntent: UIDocument.CreationIntent) -> UIAction](uidocumentviewcontroller/launchoptions-swift.class/createdocumentaction(withintent:).md)
  Creates an action that uses the specified intent.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var launchOptions: UIDocumentViewController.LaunchOptions](uidocumentviewcontroller/launchoptions-swift.property.md)
  Options that customize a document-based app’s launch view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentviewcontroller/launchoptions-swift.class)*