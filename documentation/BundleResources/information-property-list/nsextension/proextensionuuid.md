# ProExtensionUUID

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A UUID string that uniquely identifies your extension to the Compressor app.

**Availability**:
- ProVideo Encoder Extensions 1.0+
- ProVideo Workflow Extensions 1.0+

## Details

- **Name**: `ProExtensionUUID`
- **Type**: string

#### Discussion

The value for this key is a placeholder UUID the Xcode template generates. Each extension must have a unique UUID. When you build an extension for the first time, the build script in the Xcode template replaces the placeholder UUID with a new UUID. The new UUID fulfills the uniqueness and persistence requirement for `ProExtensionUUID`. For subsequent rebuilds, the UUID stays the same because the Compressor app uses this UUID to differentiate between previously saved and newly discovered extensions.

## See Also

### Professional Video Applications
- [ProExtensionAttributes](./proextensionattributes.md)
  A dictionary that specifies the minimum size of the floating window in which Final Cut Pro hosts the extension view.
- [ProExtensionPrincipalClass](./proextensionprincipalclass.md)
  The name of the class with the principal implementation of your extension.
- [ProExtensionPrincipalViewControllerClass](./proextensionprincipalviewcontrollerclass.md)
  The name of the principal view controller class of your extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsextension/proextensionuuid)*