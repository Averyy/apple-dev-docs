# QLPreviewController

**Framework**: Quick Look  
**Kind**: class  
**Role**: Class

A specialized view controller for previewing an item.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class QLPreviewController
```

```objc
@interface QLPreviewController : UIViewController
```

#### Overview

A `QLPreviewController` can display previews for many common file types, including the following:

- iWork documents
- Microsoft Office documents
- Rich text format, or RTF, documents
- PDF files
- Images
- Text files with a uniform type identifier that conforms to the `public.text` type. To learn more, see [Uniform Type Identifiers](../UniformTypeIdentifiers/UniformTypeIdentifiers.md).
- Comma-separated values, or CSV, files
- 3D models in the USDZ format with both standalone and AR views for viewing the model

> **Note**:  The list of supported common file types may change between operating system releases. In addition, you can enable previews for your own file types by implementing your own preview extension.

##### Providing data to a preview controller

To use a preview controller, you need to provide a data source object. The data source provides preview items to the controller and tells it how many items to include in a preview navigation list. If there’s more than one item in the list, a controller displays navigation arrows to let the user switch among the items. If you push a preview controller into view using a navigation controller, you can provide buttons in the navigation bar for moving through the navigation list.

For details on providing items to a preview controller, see [`QLPreviewControllerDataSource`](./qlpreviewcontrollerdatasource.md) and [`QLPreviewItem`](./qlpreviewitem.md).

##### Presenting a preview controller

You can present a `QLPreviewController` modally by calling [`present(_:animated:completion:)`](../UIKit/uiviewcontroller/present%28_,animated,completion%29.md) from a presenting [`UIViewController`](../UIKit/uiviewcontroller.md), or you can push it into view using a [`UINavigationController`](../UIKit/uinavigationcontroller.md). The preview includes a title that the system derives from the last path component of the item URL. You can override it by implementing a [`previewItemTitle`](./qlpreviewitem/previewitemtitle.md) accessor for the preview item.

##### Previewing items in Mac apps built with Mac Catalyst

For Mac apps built with Mac Catalyst, presenting a `QLPreviewController` displays the preview in a [`QLPreviewPanel`](../QuickLookUI/qlpreviewpanel.md) and dims the previously active window. However, unlike on iOS devices, where displaying a preview hides the presenting view controller, the previously visible window’s content remains visible in Mac apps built with Mac Catalyst. Be sure the content is appropriate to display while the `QLPreviewPanel` is visible.

In addition, the system doesn’t display a live preview if you embed the `QLPreviewController` in another view controller. Instead, it displays a thumbnail that matches the size of the preview controller’s view.

## Topics

### Configuring a preview controller
- [var dataSource: (any QLPreviewControllerDataSource)?](./qlpreviewcontroller/datasource.md)
  The preview controller’s data source.
- [protocol QLPreviewControllerDataSource](./qlpreviewcontrollerdatasource.md)
  The protocol that a data source for a preview controller needs to adopt to provide preview items to the controller.
- [var delegate: (any QLPreviewControllerDelegate)?](./qlpreviewcontroller/delegate.md)
  The preview controller’s delegate object.
- [protocol QLPreviewControllerDelegate](./qlpreviewcontrollerdelegate.md)
  The protocol that a delegate of a preview controller needs to adopt to handle Quick Look previews.
### Managing item previews
- [class func canPreview(any QLPreviewItem) -> Bool](./qlpreviewcontroller/canpreview%28_%29.md)
  Returns a Boolean value that indicates whether the preview controller can display an item.
- [var currentPreviewItem: (any QLPreviewItem)?](./qlpreviewcontroller/currentpreviewitem.md)
  The item displaying in the Quick Look preview controller.
- [var currentPreviewItemIndex: Int](./qlpreviewcontroller/currentpreviewitemindex.md)
  The index within the preview item navigation list of the item displaying in the Quick Look preview controller.
- [func refreshCurrentPreviewItem()](./qlpreviewcontroller/refreshcurrentpreviewitem%28%29.md)
  Asks the Quick Look preview controller to recompute the display of the current preview item.
- [func reloadData()](./qlpreviewcontroller/reloaddata%28%29.md)
  Asks the preview controller to reload its data from its data source.

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

### Previews
- [protocol QLPreviewItem](../QuickLookUI/qlpreviewitem.md)
  A protocol that defines a set of properties you implement to make a preview of your app’s content.
- [class QLPreviewSceneActivationConfiguration](./qlpreviewsceneactivationconfiguration.md)
  A scene configuration to preview items at the specified URLs.
- [Previews or thumbnail images for macOS 10.14 or earlier](./previews-or-thumbnail-images-for-macos-10-14-or-earlier.md)
  Create thumbnail images or previews of common files and custom file types in earlier versions of macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller)*