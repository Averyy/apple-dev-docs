# SMJobCopyDictionary(_:_:)

**Framework**: Service Management  
**Kind**: func  
**Role**: Function

Copies the job description dictionary for the specified job label.

**Availability**:
- iOS 3.0+ - Deprecated in 8.0
- iPadOS 3.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.6+ - Deprecated in 10.10

## Declaration

```swift
func SMJobCopyDictionary(_ domain: CFString!, _ jobLabel: CFString) -> Unmanaged<CFDictionary>!
```

```c
extern CFDictionaryRefSMJobCopyDictionary(CFStringRef domain, CFStringRef jobLabel);
```

## Return Value

A new dictionary describing the job, or `NULL` if the system couldn’t find the job. The caller must release the dictionary.

## Parameters

- `domain`: The job’s domain (for example, [`kSMDomainSystemLaunchd`](./ksmdomainsystemlaunchd.md)).
- `jobLabel`: The label identifier of the job to copy.

## See Also

### Deprecated Functions
- [func SMCopyAllJobDictionaries(CFString!) -> Unmanaged<CFArray>!](./smcopyalljobdictionaries%28_%29.md)
  Copies the job description dictionaries for all jobs in the specified domain.
- [func SMJobRemove(CFString!, CFString, UnsafeMutableRawPointer!, Bool, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./smjobremove%28_,_,_,_,_%29.md)
  Removes the job with the specified label from the specified domain.
- [func SMJobSubmit(CFString!, CFDictionary, UnsafeMutableRawPointer!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./smjobsubmit%28_,_,_,_%29.md)
  Submits the specified job to the specified domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smjobcopydictionary(_:_:))*