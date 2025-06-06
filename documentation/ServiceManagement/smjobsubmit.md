# SMJobSubmit(_:_:_:_:)

**Framework**: Service Management  
**Kind**: func

Submits the specified job to the specified domain.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+

## Declaration

```swift
func SMJobSubmit(_ domain: CFString!, _ job: CFDictionary, _ auth: AuthorizationRef!, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

#### Return Value

Returns true if the system successfully submits the job, otherwise `false`.

## Parameters

- `domain`: The job’s domain (for example,  ).
- `job`: A dictionary describing a job.
- `auth`: domain is  .
- `outError`: An output reference to a   describing the specific error when submitting the job, or   if no error occurred. It’s the responsibility of the app to release the error reference. This argument can be  .

## See Also

- [func SMCopyAllJobDictionaries(CFString!) -> Unmanaged<CFArray>!](smcopyalljobdictionaries(_:).md)
  Copies the job description dictionaries for all jobs in the specified domain.
- [func SMJobCopyDictionary(CFString!, CFString) -> Unmanaged<CFDictionary>!](smjobcopydictionary(_:_:).md)
  Copies the job description dictionary for the specified job label.
- [func SMJobRemove(CFString!, CFString, UnsafeMutableRawPointer!, Bool, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](smjobremove(_:_:_:_:_:).md)
  Removes the job with the specified label from the specified domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smjobsubmit(_:_:_:_:))*