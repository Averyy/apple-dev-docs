# UIDocumentPickerExtensionViewController

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

The principal class for the Document Picker View Controller extension.

**Availability**:
- iOS 8.0+ - Deprecated in 14.0
- iPadOS 8.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`NSFileProviderExtension`](../FileProvider/nsfileproviderextension.md) instead.

## Declaration

```swift
@MainActor
class UIDocumentPickerExtensionViewController
```

```objc
@interface UIDocumentPickerExtensionViewController : UIViewController
```

#### Overview

The Document Picker View Controller extension can perform *import* and *export* operations on its own. If you want to support *open* and *move* operations, you must pair it with a File Provider extension.

When creating a Document Picker extension, you must subclass [`UIDocumentPickerExtensionViewController`](./uidocumentpickerextensionviewcontroller.md) to provide the document picker’s user interface. Your subclass presents a list of available documents and destinations to the user. When the user makes a selection, you trigger the file transfer and pass the selected URL back to the host app.

For more information on creating Document Picker extensions, see [Document Provider](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/FileProvider.html#//apple_ref/doc/uid/TP40014214-CH18).

## Topics

### Managing the user interface
- [func dismissGrantingAccess(to: URL?)](./uidocumentpickerextensionviewcontroller/dismissgrantingaccess%28to%29.md)
  Dismisses the document picker.
- [var documentPickerMode: UIDocumentPickerMode](./uidocumentpickerextensionviewcontroller/documentpickermode.md)
  The document picker’s file-transfer operation. (read-only)
- [var documentStorageURL: URL?](./uidocumentpickerextensionviewcontroller/documentstorageurl.md)
  The root URL for documents provided by the corresponding File Provider extension. (read-only)
- [var originalURL: URL?](./uidocumentpickerextensionviewcontroller/originalurl.md)
  The URL of the file to be exported. (read-only)
- [func prepareForPresentation(in: UIDocumentPickerMode)](./uidocumentpickerextensionviewcontroller/prepareforpresentation%28in%29.md)
  Performs any custom configuration of the document picker view controller.
- [var providerIdentifier: String](./uidocumentpickerextensionviewcontroller/provideridentifier.md)
  An identifier shared by this Document Picker extension and its corresponding File Provider extension. (read-only)
- [var validTypes: [String]?](./uidocumentpickerextensionviewcontroller/validtypes.md)
  An array of valid uniform type identifiers.

## Relationships

### Inherits From
- [UIViewController](./uiviewcontroller.md)
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
- [UIActivityItemsConfigurationProviding](./uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](./uiappearancecontainer.md)
- [UIContentContainer](./uicontentcontainer.md)
- [UIFocusEnvironment](./uifocusenvironment.md)
- [UIPasteConfigurationSupporting](./uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](./uiresponderstandardeditactions.md)
- [UIStateRestoring](./uistaterestoring.md)
- [UITraitChangeObservable](./uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](./uitraitenvironment.md)
- [UIUserActivityRestoring](./uiuseractivityrestoring.md)

## See Also

### Document provider
- [class NSFileProviderExtension](../FileProvider/nsfileproviderextension.md)
  The principal class for the nonreplicated File Provider extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller)*