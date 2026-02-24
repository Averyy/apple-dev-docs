# Service Management

**Framework**: Service Management  
**Kind**: module

Manage startup items, launch agents, and launch daemons from within an app.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

#### Overview

Use Service Management to install and observe the permission settings of three supplemental helper executables that macOS supports. You can use all three of these to provide additional functionality related to your app, from inside your app’s bundle:

- **LoginItems**: An app that `launchd` starts when the user logs in. A `LoginItem` is an app that continues running until the user logs out or manually quits. Its primary purpose is to enable the system to launch helper executables automatically
- **LaunchAgents**: Processes that run on behalf of the currently logged-in user. `launchd`, a system-level process, manages Agents. Agents can communicate with other processes in the same user session and with system-wide daemons in the system context.
- **LaunchDaemons**: A stand-alone background process that `launchd` manages on behalf of the user and which runs as root and may run before any users have logged on to the system. A daemon doesn’t interact with a user process directly; it can only respond to requests made by user processes in the form of a low-level request, such as a system request, for example [`XPC`](https://developer.apple.com/documentation/Foundation/xpc), low-level Interprocess Communications system.

## Topics

### Essentials
- [Updating helper executables from earlier versions of macOS](updating-helper-executables-from-earlier-versions-of-macos.md)
  Simplify your app’s helper executables and support new authorization controls.
- [Updating your app package installer to use the new Service Management API](updating-your-app-package-installer-to-use-the-new-service-management-api.md)
  Learn about the Service Management API with a GUI-less agent app.
### Management
- [class SMAppService](smappservice.md)
  An object the framework uses to control helper executables that live inside an app’s main bundle.
- [func SMJobBless(CFString!, CFString, AuthorizationRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](smjobbless(_:_:_:_:).md)
  Submits the executable for the given label as a job to `launchd`.
- [Authorization Constants](authorization-constants.md)
  Constants that describe the ability to authorize helper executables or modify daemon applications.
- [Property List Keys](property-list-keys.md)
  Property list keys that describe the kinds of applications, daemons, and helper executables the framework manages.
### Enablement
- [func SMLoginItemSetEnabled(CFString, Bool) -> Bool](smloginitemsetenabled(_:_:).md)
  Enables a helper executable in the main app-bundle directory.
### Status
- [SMAppService.Status](smappservice/status-swift.enum.md)
  Constants that describe the registration or authorization status of a helper executable.
### Errors
- [Service Management Errors](service-management-errors.md)
  Errors that the framework returns.
### Deprecated
- [Deprecated Symbols](deprecated-symbols.md)
### Variables
- [let SMAppServiceErrorDomain: String](smappserviceerrordomain.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/ServiceManagement)*