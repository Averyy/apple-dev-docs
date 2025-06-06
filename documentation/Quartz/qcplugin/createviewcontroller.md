# createViewController()

**Framework**: Quartz  
**Kind**: method

Creates and returns a view controller for the Settings pane of a custom patch.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func createViewController() -> QCPlugInViewController!
```

#### Return Value

A view controller for the custom patch. Quartz Composer releases the controller when it is no longer needed. If necessary, you can return a subclass of `QCPlugInViewController`, but this it not typically done.

#### Discussion

This extension to the `QCPlugInViewController` class  provides user-interface support for the Settings pane of the inspector for a custom patch. You must override this method if your custom patch provides a Settings pane. The `QCPlugInViewController` object acts as a controller for Cocoa bindings between the custom patch instance (the model) and the `NSView` that contains the controls. It loads the nib file from the bundle.

The implementation is straightforward. You allocate a `QCPlugInViewController` object, initialize it, and provide the name of the nib file that contains the user interface for the Settings pane.

Note that this method follows the Core Foundation “create” rule. See the ownership policy in [`Memory Management Programming Guide for Core Foundation`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i).

For example, if the nib file name that contains the settings pane is `MySettingsPane.nib`, the implementation is:

```objc
- (QCPlugInViewController *) createViewController
{
    return [[QCPlugInViewController alloc] initWithPlugIn:self
                                              viewNibName:@"MySettingsPane"];
}
```

## See Also

- [class func plugInKeys() -> [Any]!](qcplugin/pluginkeys.md)
  Returns the keys for the internal settings of a custom patch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/createviewcontroller())*