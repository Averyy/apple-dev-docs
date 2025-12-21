# Deprecated Symbols

**Framework**: Service Management

## Topics

### Deprecated Constants
- [let kSMErrorDomainFramework: CFString!](ksmerrordomainframework.md)
  A Service Management error domain.
- [let kSMErrorDomainIPC: CFString!](ksmerrordomainipc.md)
  A Service Management IPC error domain.
- [let kSMErrorDomainLaunchd: CFString!](ksmerrordomainlaunchd.md)
  A Service Management `launchd` error domain.
### Deprecated Functions
- [func SMCopyAllJobDictionaries(CFString!) -> Unmanaged<CFArray>!](smcopyalljobdictionaries(_:).md)
  Copies the job description dictionaries for all jobs in the specified domain.
- [func SMJobCopyDictionary(CFString!, CFString) -> Unmanaged<CFDictionary>!](smjobcopydictionary(_:_:).md)
  Copies the job description dictionary for the specified job label.
- [func SMJobRemove(CFString!, CFString, UnsafeMutableRawPointer!, Bool, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](smjobremove(_:_:_:_:_:).md)
  Removes the job with the specified label from the specified domain.
- [func SMJobSubmit(CFString!, CFDictionary, UnsafeMutableRawPointer!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](smjobsubmit(_:_:_:_:).md)
  Submits the specified job to the specified domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/deprecated-symbols)*