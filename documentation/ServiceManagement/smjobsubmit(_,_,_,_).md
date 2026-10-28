# SMJobSubmit(_:_:_:_:)

**Framework**: Service Management  
**Kind**: func  
**Role**: Function

Submits the specified job to the specified domain.

**Availability**:
- iOS 3.0+ - Deprecated in 8.0
- iPadOS 3.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.6+ - Deprecated in 10.10

## Declaration

*Mac Catalyst*

```swift
func SMJobSubmit(_ domain: CFString!, _ job: CFDictionary, _ auth: UnsafeMutableRawPointer!, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

*macOS*

```swift
func SMJobSubmit(_ domain: CFString!, _ job: CFDictionary, _ auth: AuthorizationRef!, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

*Mac Catalyst*

```c
extern Boolean SMJobSubmit(CFStringRef domain, CFDictionaryRef job, void *auth, CFErrorRef*outError);
```

*macOS*

```c
extern Boolean SMJobSubmit(CFStringRef domain, CFDictionaryRef job, AuthorizationRef auth, CFErrorRef*outError);
```

## Return Value

Returns true if the system successfully submits the job, otherwise `false`.

## Parameters

- `domain`: The job’s domain (for example, [`kSMDomainSystemLaunchd`](./ksmdomainsystemlaunchd.md)).
- `job`: A dictionary describing a job.
- `auth`: An `AuthorizationRef` containing the [`kSMRightModifySystemDaemons`](./ksmrightmodifysystemdaemons.md) right if the specified

  domain is [`kSMDomainSystemLaunchd`](./ksmdomainsystemlaunchd.md).
- `outError`: An output reference to a `CFErrorRef` describing the specific error when submitting the job, or `NULL` if no error occurred. It’s the responsibility of the app to release the error reference. This argument can be `NULL`.

## See Also

### Deprecated Functions
- [func SMCopyAllJobDictionaries(CFString!) -> Unmanaged<CFArray>!](./smcopyalljobdictionaries%28_%29.md)
  Copies the job description dictionaries for all jobs in the specified domain.
- [func SMJobCopyDictionary(CFString!, CFString) -> Unmanaged<CFDictionary>!](./smjobcopydictionary%28_,_%29.md)
  Copies the job description dictionary for the specified job label.
- [func SMJobRemove(CFString!, CFString, UnsafeMutableRawPointer!, Bool, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./smjobremove%28_,_,_,_,_%29.md)
  Removes the job with the specified label from the specified domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smjobsubmit(_:_:_:_:))*