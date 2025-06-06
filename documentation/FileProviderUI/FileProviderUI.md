# File Provider UI

**Framework**: File Provider UI  
**Kind**: module

Add actions to the document browser’s context menu.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

#### Overview

Use the File Provider UI extension to add custom actions to your File Provider extension. These actions appear if the user long presses an item while browsing your file provider’s content. When the user selects your action, the system displays your custom user interface, where the user completes the action. After the user is finished, you must explicitly cancel or complete the action.

For more about File Provider extensions, see [`File Provider`](https://developer.apple.com/documentation/FileProvider).

For more about creating extensions, see [`App Extension Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214).

## Topics

### Document Browser Customization
- [Adding Actions to the Context Menu](adding-actions-to-the-context-menu.md)
  Present custom actions from your File Provider extension in the system’s file browser.
- [class FPUIActionExtensionViewController](fpuiactionextensionviewcontroller.md)
  The custom user interface used to perform a selected action.
### Errors
- [enum FPUIExtensionErrorCode](fpuiextensionerrorcode.md)
  The error codes for errors raised by the File Provider UI extension.
- [let FPUIErrorDomain: String](fpuierrordomain.md)
  The error domain for errors raised by the File Provider UI extension.
### Reference
- [FileProviderUI Data Types](fileproviderui-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/FileProviderUI)*