# BERenderingProcess

**Framework**: BrowserEngineKit  
**Kind**: class  
**Role**: Class

An object that represents a running browser rendering extension process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```objc
@interface BERenderingProcess : NSObject
```

## Overview

A browser app may have one or more rendering extensions, each of which need a separate bundle identifier. The app can launch only one instance of each of rendering extension.

## Topics

### Creating and invalidating extension processes
- [+ renderingProcessWithBundleID:interruptionHandler:completion:](./berenderingprocess/renderingprocesswithbundleid_interruptionhandler_completion_.md)
  Launches a rendering extension process asynchronously.
- [+ renderingProcessWithInterruptionHandler:completion:](./berenderingprocess/renderingprocesswithinterruptionhandler_completion_.md)
  Launches a rendering extension process asynchronously.
- [- invalidate](./berenderingprocess/invalidate.md)
  Stops the rendering process.
### Creating XPC connections
- [- makeLibXPCConnectionError:](./berenderingprocess/makelibxpcconnectionerror_.md)
  Creates a new XPC connection to the extension process.
### Coordinating processes
- [- grantCapability:error:](./berenderingprocess/grantcapability_error_.md)
  Grants the specified capability to the process.
- [- grantCapability:error:invalidationHandler:](./berenderingprocess/grantcapability_error_invalidationhandler_.md)
  Grants the specified capability to the process, invoking the handler when the capability becomes invalid.
- [- createVisibilityPropagationInteraction](./berenderingprocess/createvisibilitypropagationinteraction.md)
  Returns an interaction that associates a view with the rendering process.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [BEExtensionProcess](./beextensionprocess.md)

## See Also

### Host app representations
- [BEWebContentProcess](./bewebcontentprocess.md)
  A class that processes webpage content in an app extension.
- [BENetworkingProcess](./benetworkingprocess.md)
  An object that represents a networking extension process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/berenderingprocess)*