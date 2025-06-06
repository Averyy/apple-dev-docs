# WebPlugInContainer

**Framework**: Objective-C Runtime

`WebPlugInContainer` is an informal protocol that enables a plug-in to send messages to the application.

## Topics

### Performing actions on the enclosing container
- [func webPlugInContainerLoad(URLRequest!, inFrame: String!)](nsobject-swift.class/webplugincontainerload(_:inframe:).md)
  Loads a URL into a web frame.
- [func webPlugInContainerShowStatus(String!)](nsobject-swift.class/webplugincontainershowstatus(_:).md)
  Tells the container to show a status message.
### Obtaining information about the container
- [var webFrame: WebFrame!](nsobject-swift.class/webframe.md)
  Returns the `WebFrame` that contains the plug-in.
- [var webPlugInContainerSelectionColor: NSColor!](nsobject-swift.class/webplugincontainerselectioncolor.md)
  Returns the plug-in selection color.

## See Also

- [WebKit Objective-C Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)
- [WebPlugIn](webplugin.md)
  The `WebPlugIn` informal protocol defines methods that enable interaction between an application using the WebKit framework and any WebKit-based plug-ins it may use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/webplugincontainer)*