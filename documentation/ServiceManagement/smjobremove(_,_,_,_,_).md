# SMJobRemove(_:_:_:_:_:)

**Framework**: Service Management  
**Kind**: func  
**Role**: Function

Removes the job with the specified label from the specified domain.

**Availability**:
- iOS 3.0+ - Deprecated in 8.0
- iPadOS 3.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.6+ - Deprecated in 10.10

## Declaration

*Mac Catalyst*

```swift
func SMJobRemove(_ domain: CFString!, _ jobLabel: CFString, _ auth: UnsafeMutableRawPointer!, _ wait: Bool, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

*macOS*

```swift
func SMJobRemove(_ domain: CFString!, _ jobLabel: CFString, _ auth: AuthorizationRef!, _ wait: Bool, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

*Mac Catalyst*

```c
extern Boolean SMJobRemove(CFStringRef domain, CFStringRef jobLabel, void *auth, Boolean wait, CFErrorRef*outError);
```

*macOS*

```c
extern Boolean SMJobRemove(CFStringRef domain, CFStringRef jobLabel, AuthorizationRef auth, Boolean wait, CFErrorRef*outError);
```

#### Return Value

Returns `true` if the system successfully removes the job, otherwise `false`.

#### Discussion

If the job is currently running, it conditionally blocks until the running process has exited.

## Parameters

- `domain`: The job’s domain (for example, [`kSMDomainSystemLaunchd`](./ksmdomainsystemlaunchd.md)).
- `jobLabel`: The label identifier of the job to remove.
- `auth`: An `AuthorizationRef` containing the [`kSMRightModifySystemDaemons`](./ksmrightmodifysystemdaemons.md) right if the specified domain is [`kSMDomainSystemLaunchd`](./ksmdomainsystemlaunchd.md).
- `wait`: Pass `true` to block until the process for the specified job has exited.
- `outError`: An output reference to a `CFErrorRef` describing the specific error when removing the job, or `NULL` if no error occurred. It’s the responsibility of the app to release the error reference. This argument can be `NULL`.

## See Also

### Deprecated Functions
- [func SMCopyAllJobDictionaries(CFString!) -> Unmanaged<CFArray>!](./smcopyalljobdictionaries%28_%29.md)
  Copies the job description dictionaries for all jobs in the specified domain.
- [func SMJobCopyDictionary(CFString!, CFString) -> Unmanaged<CFDictionary>!](./smjobcopydictionary%28_,_%29.md)
  Copies the job description dictionary for the specified job label.
- [func SMJobSubmit(CFString!, CFDictionary, UnsafeMutableRawPointer!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./smjobsubmit%28_,_,_,_%29.md)
  Submits the specified job to the specified domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smjobremove(_:_:_:_:_:))*