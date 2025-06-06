# SMCopyAllJobDictionaries(_:)

**Framework**: Service Management  
**Kind**: func

Copies the job description dictionaries for all jobs in the specified domain.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+

## Declaration

```swift
func SMCopyAllJobDictionaries(_ domain: CFString!) -> Unmanaged<CFArray>!
```

#### Return Value

A new array containing all job dictionaries, or `NULL` if an error occurred. The caller must release the array.

## Parameters

- `domain`: The job’s domain (for example,  ).

## See Also

- [func SMJobCopyDictionary(CFString!, CFString) -> Unmanaged<CFDictionary>!](smjobcopydictionary(_:_:).md)
  Copies the job description dictionary for the specified job label.
- [func SMJobRemove(CFString!, CFString, UnsafeMutableRawPointer!, Bool, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](smjobremove(_:_:_:_:_:).md)
  Removes the job with the specified label from the specified domain.
- [func SMJobSubmit(CFString!, CFDictionary, UnsafeMutableRawPointer!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](smjobsubmit(_:_:_:_:).md)
  Submits the specified job to the specified domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smcopyalljobdictionaries(_:))*