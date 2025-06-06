# ProExtensionPrincipalViewControllerClass

**Framework**: Bundle Resources  
**Kind**: typealias

The name of the principal view controller class of your extension.

**Availability**:
- ProVideo Encoder Extensions 1.0+
- ProVideo Workflow Extensions 1.0+

#### Discussion

This key provides the name of the primary view controller class of your extension that adopts the [`NSViewController`](https://developer.apple.com/documentation/AppKit/NSViewController) protocol. When you create an extension, the Xcode template automatically includes this key in the workflow extension information property list. You only modify the value of this key when you rename the primary view controller class in your extension.

## See Also

- [ProExtensionAttributes](information-property-list/nsextension/proextensionattributes.md)
  A dictionary that specifies the minimum size of the floating window in which Final Cut Pro hosts the extension view.
- [ProExtensionPrincipalClass](information-property-list/nsextension/proextensionprincipalclass.md)
  The name of the class with the principal implementation of your extension.
- [ProExtensionUUID](information-property-list/nsextension/proextensionuuid.md)
  A UUID string that uniquely identifies your extension to the Compressor app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsextension/proextensionprincipalviewcontrollerclass)*