# SMAppService

**Framework**: Service Management  
**Kind**: class  
**Role**: Class

An object the framework uses to control helper executables that live inside an app’s main bundle.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
class SMAppService
```

```objc
@interface SMAppService : NSObject
```

## Overview

In macOS 13 and later, use `SMAppService` to register and control `LoginItems`, `LaunchAgents`, and `LaunchDaemons` as helper executables for your app. When converting code from earlier versions of macOS, use an `SMAppService` object and select one of the following methods depending on the type of service your helper executable provides:

- For `SMAppServices` initialized as `LoginItems`, the [`register()`](./smappservice/register%28%29.md) and [`unregister()`](./smappservice/unregister%28%29.md) APIs provide a replacement for [`SMLoginItemSetEnabled(_:_:)`](./smloginitemsetenabled%28_,_%29.md).
- For `SMAppServices` initialized as `LaunchAgents`, the [`register()`](./smappservice/register%28%29.md) and [`unregister()`](./smappservice/unregister%28%29.md) methods provide a replacement for installing property lists in `~/Library/LaunchAgents` or `/Library/LaunchAgents`.
- For `SMAppServices` initialized as `LaunchDaemons`, the [`register()`](./smappservice/register%28%29.md) and [`unregister()`](./smappservice/unregister%28%29.md) methods provide a replacement for installing property lists in `/Library/LaunchDaemons`.

## Topics

### Registering services
- [func register() throws](./smappservice/register%28%29.md)
  Registers the service so it can begin launching subject to user approval.
- [func unregister() throws](./smappservice/unregister%28%29.md)
  Unregisters the service so the system no longer launches it.
- [func unregister(completionHandler: ((any Error)?) -> Void)](./smappservice/unregister%28completionhandler%29.md)
  Unregisters the service so the system no longer launches it and calls a completion handler you provide with the resulting error value.
### Managing apps
- [class var mainApp: SMAppService](./smappservice/mainapp.md)
  An app service object that corresponds to the main application as a login item.
- [class func agent(plistName: String) -> Self](./smappservice/agent%28plistname%29.md)
  Initializes an app service object with a launch agent with the property list name you provide.
- [class func daemon(plistName: String) -> Self](./smappservice/daemon%28plistname%29.md)
  Initializes an app service object with a launch daemon with the property list name you provide.
- [class func loginItem(identifier: String) -> Self](./smappservice/loginitem%28identifier%29.md)
  Initializes an app service object for a login item corresponding to the bundle with the identifier you provide.
### Interacting with System Settings
- [class func openSystemSettingsLoginItems()](./smappservice/opensystemsettingsloginitems%28%29.md)
  Opens System Settings to the Login Items control panel.
### Getting the state of the service
- [var status: SMAppService.Status](./smappservice/status-swift.property.md)
  A property that describes registration or authorization state of the service.
- [SMAppService.Status](./smappservice/status-swift.enum.md)
  Constants that describe the registration or authorization status of a helper executable.
### Checking authorization for earlier OS version login items
- [class func statusForLegacyPlist(at: URL) -> SMAppService.Status](./smappservice/statusforlegacyplist%28at%29.md)
  Check the authorization status of an earlier OS version login item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Management
- [func SMJobBless(CFString!, CFString, AuthorizationRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./smjobbless%28_,_,_,_%29.md)
  Submits the executable for the given label as a job to `launchd`.
- [Authorization Constants](./authorization-constants.md)
  Constants that describe the ability to authorize helper executables or modify daemon applications.
- [Property List Keys](./property-list-keys.md)
  Property list keys that describe the kinds of applications, daemons, and helper executables the framework manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smappservice)*