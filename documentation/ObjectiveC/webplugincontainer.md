# WebPlugInContainer

**Framework**: Objective-C Runtime  
**Role**: API Collection

`WebPlugInContainer` is an informal protocol that enables a plug-in to send messages to the application.

## Topics

### Performing actions on the enclosing container
- [func webPlugInContainerLoad(URLRequest!, inFrame: String!)](./nsobject-swift.class/webplugincontainerload%28_,inframe%29.md)
  Loads a URL into a web frame.
- [func webPlugInContainerShowStatus(String!)](./nsobject-swift.class/webplugincontainershowstatus%28_%29.md)
  Tells the container to show a status message.
### Obtaining information about the container
- [var webFrame: WebFrame!](./nsobject-swift.class/webframe.md)
  Returns the `WebFrame` that contains the plug-in.
- [var webPlugInContainerSelectionColor: NSColor!](./nsobject-swift.class/webplugincontainerselectioncolor.md)
  Returns the plug-in selection color.

## See Also

### Related Documentation
- [WebKit Objective-C Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)
### Interacting with Web Plug-ins
- [WebPlugIn](./webplugin.md)
  The `WebPlugIn` informal protocol defines methods that enable interaction between an application using the WebKit framework and any WebKit-based plug-ins it may use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/webplugincontainer)*