# BEWebContentProcess

**Framework**: BrowserEngineKit  
**Kind**: class  
**Role**: Class

A class that processes webpage content in an app extension.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```objc
@interface BEWebContentProcess : NSObject
```

## Overview

A browser app may launch multiple web content extension processes, and each instance of this class represents a separate process.

## Topics

### Creating and invalidating extension processes
- [+ webContentProcessWithBundleID:interruptionHandler:completion:](./bewebcontentprocess/webcontentprocesswithbundleid_interruptionhandler_completion_.md)
  Launches a web content extension process asynchronously.
- [+ webContentProcessWithInterruptionHandler:completion:](./bewebcontentprocess/webcontentprocesswithinterruptionhandler_completion_.md)
  Launches a web content extension process asynchronously.
- [- invalidate](./bewebcontentprocess/invalidate.md)
  Stops the web content process.
### Creating XPC connections
- [- makeLibXPCConnectionError:](./bewebcontentprocess/makelibxpcconnectionerror_.md)
  Creates a new XPC connection to the extension process.
### Coordinating processes
- [- grantCapability:error:](./bewebcontentprocess/grantcapability_error_.md)
  Grants the specified capability to the process.
- [- grantCapability:error:invalidationHandler:](./bewebcontentprocess/grantcapability_error_invalidationhandler_.md)
  Grants the specified capability to the process, invoking the handler when the capability becomes invalid.
- [- createVisibilityPropagationInteraction](./bewebcontentprocess/createvisibilitypropagationinteraction.md)
  Returns an interaction that associates a view with the web content process.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [BEExtensionProcess](./beextensionprocess.md)

## See Also

### Host app representations
- [BENetworkingProcess](./benetworkingprocess.md)
  An object that represents a networking extension process.
- [BERenderingProcess](./berenderingprocess.md)
  An object that represents a running browser rendering extension process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebcontentprocess)*