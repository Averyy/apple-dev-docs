# ProExtensionUUID

**Framework**: Bundle Resources  
**Kind**: typealias

A UUID string that uniquely identifies your extension to the Compressor app.

**Availability**:
- ProVideo Encoder Extensions 1.0+
- ProVideo Workflow Extensions 1.0+

#### Discussion

The value for this key is a placeholder UUID the Xcode template generates. Each extension must have a unique UUID. When you build an extension for the first time, the build script in the Xcode template replaces the placeholder UUID with a new UUID. The new UUID fulfills the uniqueness and persistence requirement for `ProExtensionUUID`. For subsequent rebuilds, the UUID stays the same because the Compressor app uses this UUID to differentiate between previously saved and newly discovered extensions.

## See Also

- [ProExtensionAttributes](information-property-list/nsextension/proextensionattributes.md)
  A dictionary that specifies the minimum size of the floating window in which Final Cut Pro hosts the extension view.
- [ProExtensionPrincipalClass](information-property-list/nsextension/proextensionprincipalclass.md)
  The name of the class with the principal implementation of your extension.
- [ProExtensionPrincipalViewControllerClass](information-property-list/nsextension/proextensionprincipalviewcontrollerclass.md)
  The name of the principal view controller class of your extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsextension/proextensionuuid)*