# ProExtensionPrincipalViewControllerClass

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The name of the principal view controller class of your extension.

**Availability**:
- ProVideo Encoder Extensions 1.0+
- ProVideo Workflow Extensions 1.0+

## Details

- **Name**: `ProExtensionPrincipalViewControllerClass`
- **Type**: string

#### Discussion

This key provides the name of the primary view controller class of your extension that adopts the [`NSViewController`](../../../AppKit/nsviewcontroller.md) protocol. When you create an extension, the Xcode template automatically includes this key in the workflow extension information property list. You only modify the value of this key when you rename the primary view controller class in your extension.

## See Also

### Professional Video Applications
- [ProExtensionAttributes](./proextensionattributes.md)
  A dictionary that specifies the minimum size of the floating window in which Final Cut Pro hosts the extension view.
- [ProExtensionPrincipalClass](./proextensionprincipalclass.md)
  The name of the class with the principal implementation of your extension.
- [ProExtensionUUID](./proextensionuuid.md)
  A UUID string that uniquely identifies your extension to the Compressor app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsextension/proextensionprincipalviewcontrollerclass)*