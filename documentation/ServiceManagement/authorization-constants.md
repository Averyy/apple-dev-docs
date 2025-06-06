# Authorization Constants

**Framework**: Service Management

Constants that describe the ability to authorize helper executables or modify daemon applications.

## Topics

### Constants
- [var kSMRightBlessPrivilegedHelper: String](ksmrightblessprivilegedhelper.md)
  The authorization rights key for approving and installing a privileged helper tool.
- [var kSMRightBlessPrivilegedHelper: String](ksmrightblessprivilegedhelper.md)
  The authorization rights key for approving and installing a privileged helper tool.
- [var kSMRightModifySystemDaemons: String](ksmrightmodifysystemdaemons.md)
  The authorization rights key for modifying system daemons.
- [var kSMRightModifySystemDaemons: String](ksmrightmodifysystemdaemons.md)
  The authorization rights key for modifying system daemons.

## See Also

- [class SMAppService](smappservice.md)
  An object the framework uses to control helper executables that live inside an app’s main bundle.
- [func SMJobBless(CFString!, CFString, AuthorizationRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](smjobbless(_:_:_:_:).md)
  Submits the executable for the given label as a job to `launchd`.
- [Property List Keys](property-list-keys.md)
  Property list keys that describe the kinds of applications, daemons, and helper executables the framework manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/authorization-constants)*