# CXErrorDomainCallDirectoryManager

**Framework**: CallKit  
**Kind**: var  
**Role**: Global Variable

Domain for errors when interacting with a call directory manager.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
let CXErrorDomainCallDirectoryManager: String
```

```c
extern NSErrorDomain const CXErrorDomainCallDirectoryManager;
```

#### Discussion

See [CallKit Constants](./callkit-constants.md) for possible error codes.

## See Also

### Errors
- [CXCallDirectoryManager.EnabledStatus](./cxcalldirectorymanager/enabledstatus.md)
  The enabled status of a Call Directory app extension, as reported by the [`getEnabledStatusForExtension(withIdentifier:completionHandler:)`](./cxcalldirectorymanager/getenabledstatusforextension%28withidentifier,completionhandler%29.md) method.
- [struct CXErrorCodeCallDirectoryManagerError](./cxerrorcodecalldirectorymanagererror-swift.struct.md)
  Errors when interacting with a call directory manager.
- [CXErrorCodeCallDirectoryManagerError.Code](./cxerrorcodecalldirectorymanagererror-swift.struct/code.md)
  Error codes the CallKit framework returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrordomaincalldirectorymanager)*