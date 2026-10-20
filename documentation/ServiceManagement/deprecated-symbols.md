# Deprecated Symbols

**Framework**: Service Management  
**Role**: API Collection

## Topics

### Deprecated Constants
- [let kSMErrorDomainFramework: CFString!](./ksmerrordomainframework.md)
  A Service Management error domain.
- [let kSMErrorDomainIPC: CFString!](./ksmerrordomainipc.md)
  A Service Management IPC error domain.
- [let kSMErrorDomainLaunchd: CFString!](./ksmerrordomainlaunchd.md)
  A Service Management `launchd` error domain.
### Deprecated Functions
- [func SMCopyAllJobDictionaries(CFString!) -> Unmanaged<CFArray>!](./smcopyalljobdictionaries%28_%29.md)
  Copies the job description dictionaries for all jobs in the specified domain.
- [func SMJobCopyDictionary(CFString!, CFString) -> Unmanaged<CFDictionary>!](./smjobcopydictionary%28_,_%29.md)
  Copies the job description dictionary for the specified job label.
- [func SMJobRemove(CFString!, CFString, UnsafeMutableRawPointer!, Bool, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./smjobremove%28_,_,_,_,_%29.md)
  Removes the job with the specified label from the specified domain.
- [func SMJobSubmit(CFString!, CFDictionary, UnsafeMutableRawPointer!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./smjobsubmit%28_,_,_,_%29.md)
  Submits the specified job to the specified domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/deprecated-symbols)*