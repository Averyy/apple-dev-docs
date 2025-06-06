# CXCallDirectoryManager

**Framework**: CallKit  
**Kind**: class

The programmatic interface to an object that manages a Call Directory app extension.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+

## Declaration

```swift
class CXCallDirectoryManager
```

## Topics

### Accessing the Shared Instance
- [class var sharedInstance: CXCallDirectoryManager](cxcalldirectorymanager/sharedinstance.md)
  Returns the shared call directory manager instance for the app.
### Working with a Call Directory App Extension
- [func getEnabledStatusForExtension(withIdentifier: String, completionHandler: (CXCallDirectoryManager.EnabledStatus, (any Error)?) -> Void)](cxcalldirectorymanager/getenabledstatusforextension(withidentifier:completionhandler:).md)
  Asynchronously returns the enabled status of the extension with the specified identifier.
- [func reloadExtension(withIdentifier: String, completionHandler: (((any Error)?) -> Void)?)](cxcalldirectorymanager/reloadextension(withidentifier:completionhandler:).md)
  Asynchronously reloads the extension with the specified identifier.
- [CXCallDirectoryManager.EnabledStatus](cxcalldirectorymanager/enabledstatus.md)
  The enabled status of a Call Directory app extension, as reported by the [`getEnabledStatusForExtension(withIdentifier:completionHandler:)`](cxcalldirectorymanager/getenabledstatusforextension(withidentifier:completionhandler:).md) method.
### Opening the Settings App
- [func openSettings(completionHandler: (((any Error)?) -> Void)?)](cxcalldirectorymanager/opensettings(completionhandler:).md)
  Opens the iOS Settings app and shows the Call Blocking & Identification settings.
### Errors
- [CXCallDirectoryManager.EnabledStatus](cxcalldirectorymanager/enabledstatus.md)
  The enabled status of a Call Directory app extension, as reported by the [`getEnabledStatusForExtension(withIdentifier:completionHandler:)`](cxcalldirectorymanager/getenabledstatusforextension(withidentifier:completionhandler:).md) method.
- [struct CXErrorCodeCallDirectoryManagerError](cxerrorcodecalldirectorymanagererror-swift.struct.md)
  Errors when interacting with a call directory manager.
- [CXErrorCodeCallDirectoryManagerError.Code](cxerrorcodecalldirectorymanagererror-swift.struct/code.md)
  Error codes the CallKit framework returns.
- [let CXErrorDomainCallDirectoryManager: String](cxerrordomaincalldirectorymanager.md)
  Domain for errors when interacting with a call directory manager.

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

- [Identifying and blocking calls](identifying-and-blocking-calls.md)
  Create a Call Directory app extension to identify and block incoming callers by their phone number.
- [class CXCallDirectoryProvider](cxcalldirectoryprovider.md)
  The principal object for a Call Directory app extension for a host app.
- [class CXCallDirectoryExtensionContext](cxcalldirectoryextensioncontext.md)
  A programmatic interface for adding identification and blocking entries to a Call Directory app extension.
- [protocol CXCallDirectoryExtensionContextDelegate](cxcalldirectoryextensioncontextdelegate.md)
  A collection of methods a Call Directory extension context object calls when a request fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectorymanager)*