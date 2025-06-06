# SMJobRemove(_:_:_:_:_:)

**Framework**: Service Management  
**Kind**: func

Removes the job with the specified label from the specified domain.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+

## Declaration

```swift
func SMJobRemove(_ domain: CFString!, _ jobLabel: CFString, _ auth: UnsafeMutableRawPointer!, _ wait: Bool, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

#### Return Value

Returns `true` if the system successfully removes the job, otherwise `false`.

#### Discussion

If the job is currently running, it conditionally blocks until the running process has exited.

## Parameters

- `domain`: The job’s domain (for example,  ).
- `jobLabel`: The label identifier of the job to remove.
- `auth`: An   containing the   right if the specified domain is  .
- `wait`: Pass   to block until the process for the specified job has exited.
- `outError`: An output reference to a   describing the specific error when removing the job, or   if no error occurred. It’s the responsibility of the app to release the error reference. This argument can be  .

## See Also

- [func SMCopyAllJobDictionaries(CFString!) -> Unmanaged<CFArray>!](smcopyalljobdictionaries(_:).md)
  Copies the job description dictionaries for all jobs in the specified domain.
- [func SMJobCopyDictionary(CFString!, CFString) -> Unmanaged<CFDictionary>!](smjobcopydictionary(_:_:).md)
  Copies the job description dictionary for the specified job label.
- [func SMJobSubmit(CFString!, CFDictionary, UnsafeMutableRawPointer!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](smjobsubmit(_:_:_:_:).md)
  Submits the specified job to the specified domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smjobremove(_:_:_:_:_:))*