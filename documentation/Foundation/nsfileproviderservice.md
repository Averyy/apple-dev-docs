# NSFileProviderService

**Framework**: Foundation  
**Kind**: class

A service that provides a custom communication channel between your app and a File Provider extension.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
class NSFileProviderService
```

#### Overview

To communicate, both your app and the File Provider extension must implement their part of the service:

- Your app requests the proxy object, and calls its methods.
- The File Provider extension declares the supported services and vends a proxy object that implements the protocol for each service.

The app and File Provider extension communicate using an XPC service. This service performs actions only on items managed by the File Provider extension. For more information, see [`Creating XPC Services`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingXPCServices.html#//apple_ref/doc/uid/10000172i-SW6).

##### Defining the Services Protocol

Services let you define custom actions that are not provided by Apple’s APIs. Both the app and the File Provider extension must agree upon the service’s name and protocol.  Communicate the name and protocol through an outside source (for example, posting a header file that defines both the name and protocol, or publishing a library that includes them both).

The service can be defined by either the app or the File Provider extension:

- Apps can define a service for features they would like to use. File providers can then choose to support those features by implementing the service.
- File Provider extensions can provide a service for the features they support. Apps can then choose to use the specified service.

When defining a service’s protocol, the parameters for each method must adhere to the following rules:

- The parameter’s class must conform to [`NSSecureCoding`](nssecurecoding.md).
- The parameter’s class must be defined in both the app and the File Provider extension (for example, standard system types or classes defined in a library imported by both sides).
- If a collection parameter contains types other than property list types (see [`Property List Types and Objects`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44-SW2)), declare the valid types using the [`NSXPCInterface`](nsxpcinterface.md) class’s [`classes(for:argumentIndex:ofReply:)`](nsxpcinterface/classes(for:argumentindex:ofreply:).md) method.

## Topics

### Accessing the Service
- [var name: NSFileProviderServiceName](nsfileproviderservice/name.md)
  The File Provider service’s name.
- [func getFileProviderConnection(completionHandler: (NSXPCConnection?, (any Error)?) -> Void)](nsfileproviderservice/getfileproviderconnection(completionhandler:).md)
  Asynchronously returns the service’s connection object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func getFileProviderServicesForItem(at: URL, completionHandler: ([NSFileProviderServiceName : NSFileProviderService]?, (any Error)?) -> Void)](filemanager/getfileproviderservicesforitem(at:completionhandler:).md)
  Returns the services provided by the File Provider extension that manages the item at the given URL.
- [struct NSFileProviderServiceName](nsfileproviderservicename.md)
  The name used to identify a File Provider service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileproviderservice)*