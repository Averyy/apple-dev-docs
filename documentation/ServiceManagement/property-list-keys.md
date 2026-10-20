# Property List Keys

**Framework**: Service Management  
**Role**: API Collection

Property list keys that describe the kinds of applications, daemons, and helper executables the framework manages.

## Topics

### Constants
- [let kSMDomainSystemLaunchd: CFString!](./ksmdomainsystemlaunchd.md)
  The system-level launch domain.
- [let kSMDomainUserLaunchd: CFString!](./ksmdomainuserlaunchd.md)
  The user-level launch domain.

## See Also

### Management
- [class SMAppService](./smappservice.md)
  An object the framework uses to control helper executables that live inside an app’s main bundle.
- [func SMJobBless(CFString!, CFString, AuthorizationRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./smjobbless%28_,_,_,_%29.md)
  Submits the executable for the given label as a job to `launchd`.
- [Authorization Constants](./authorization-constants.md)
  Constants that describe the ability to authorize helper executables or modify daemon applications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/property-list-keys)*