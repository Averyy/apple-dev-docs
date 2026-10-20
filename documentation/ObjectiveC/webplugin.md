# WebPlugIn

**Framework**: Objective-C Runtime  
**Role**: API Collection

The `WebPlugIn` informal protocol defines methods that enable interaction between an application using the WebKit framework and any WebKit-based plug-ins it may use.

## Topics

### Accessing the Scripting Environment
- [var objectForWebScript: Any!](./nsobject-swift.class/objectforwebscript.md)
  Returns an object that exposes the plug-in’s scripting interface.
### Using Plug-in State Information
- [func webPlugInSetIsSelected(Bool)](./nsobject-swift.class/webpluginsetisselected%28_%29.md)
  Controls plug-in behavior based on its selection.
### Controlling the Plug-in
- [func webPlugInDestroy()](./nsobject-swift.class/webplugindestroy%28%29.md)
  Prepares the plug-in for deallocation.
- [func webPlugInInitialize()](./nsobject-swift.class/webplugininitialize%28%29.md)
  Initializes the plug-in.
- [func webPlugInStart()](./nsobject-swift.class/webpluginstart%28%29.md)
  Tells the plug-in to start normal operation.
- [func webPlugInStop()](./nsobject-swift.class/webpluginstop%28%29.md)
  Tells the plug-in to stop normal operation.
### Main resource messages
- [func webPlugInMainResourceDidFailWithError((any Error)!)](./nsobject-swift.class/webpluginmainresourcedidfailwitherror%28_%29.md)
  Invoked when an error occurs loading the main resource.
- [func webPlugInMainResourceDidFinishLoading()](./nsobject-swift.class/webpluginmainresourcedidfinishloading%28%29.md)
  Invoked when the connection successfully finishes loading data.
- [func webPlugInMainResourceDidReceive(Data!)](./nsobject-swift.class/webpluginmainresourcedidreceive%28_%29-5b6f6.md)
  Invoked when the connection loads data incrementally.
- [func webPlugInMainResourceDidReceive(URLResponse!)](./nsobject-swift.class/webpluginmainresourcedidreceive%28_%29-6x7b9.md)
  Invoked when the connection receives sufficient data to construct the URL response for its request.

## See Also

### Interacting with Web Plug-ins
- [WebPlugInContainer](./webplugincontainer.md)
  `WebPlugInContainer` is an informal protocol that enables a plug-in to send messages to the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/webplugin)*