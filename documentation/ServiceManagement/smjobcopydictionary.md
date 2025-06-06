# SMJobCopyDictionary(_:_:)

**Framework**: Service Management  
**Kind**: func

Copies the job description dictionary for the specified job label.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+

## Declaration

```swift
func SMJobCopyDictionary(_ domain: CFString!, _ jobLabel: CFString) -> Unmanaged<CFDictionary>!
```

#### Return Value

A new dictionary describing the job, or `NULL` if the system couldn’t find the job. The caller must release the dictionary.

## Parameters

- `domain`: The job’s domain (for example,  ).
- `jobLabel`: The label identifier of the job to copy.

## See Also

- [func SMCopyAllJobDictionaries(CFString!) -> Unmanaged<CFArray>!](smcopyalljobdictionaries(_:).md)
  Copies the job description dictionaries for all jobs in the specified domain.
- [func SMJobRemove(CFString!, CFString, UnsafeMutableRawPointer!, Bool, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](smjobremove(_:_:_:_:_:).md)
  Removes the job with the specified label from the specified domain.
- [func SMJobSubmit(CFString!, CFDictionary, UnsafeMutableRawPointer!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](smjobsubmit(_:_:_:_:).md)
  Submits the specified job to the specified domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smjobcopydictionary(_:_:))*