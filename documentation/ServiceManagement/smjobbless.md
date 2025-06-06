# SMJobBless(_:_:_:_:)

**Framework**: Service Management  
**Kind**: func

Submits the executable for the given label as a job to `launchd`.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func SMJobBless(_ domain: CFString!, _ executableLabel: CFString, _ auth: AuthorizationRef!, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/swift/true) if the job was successfully submitted; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

`SMJobBless` submits the executable for the given label as a `launchd` job. This function removes the need for a `setuid(_:)` helper invoked through [`AuthorizationExecuteWithPrivileges`](https://developer.apple.com/documentation/security/1540038-authorizationexecutewithprivileg) in order to install a `launchd` property list. If the job is already installed, this methods returns [`true`](https://developer.apple.com/documentation/swift/true).

In order to use this function, the app must meet the following requirements:

1. Xcode must sign both the calling app and target executable tool.
2. The calling app’s `Info.plist` must include an [`SMPrivilegedExecutables`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SMPrivilegedExecutables) dictionary of strings. Each string is a textual representation of a code signing requirement the system uses to determine whether the app owns the privileged tool once installed (for example, in order for subsequent versions to update the installed version).

Each key of `SMPrivilegedExecutables` is a reverse-DNS label for the helper tool that must be globally unique.

1. The helper tool must have an embedded `Info.plist` containing an [`SMAuthorizedClients`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SMAuthorizedClients) array of strings. Each string is a textual representation of a code signing requirement describing a client allowed to add and remove the tool.
2. The helper tool must have an embedded launchd property list. The only required key in this property list is the `Label` key. When the Service Management framework extracts the `launchd` property list and writes it to disk, it sets the key for `ProgramArguments` to an array of 1 element that points to a standard location. You can’t specify your own program arguments, so don’t rely on the system passing custom command line arguments to your tool. Pass any parameters through an inter-process communication (IPC) channel.
3. The helper tool must reside in the Contents/Library/LaunchServices directory inside the application bundle, and its name must be its launchd job label. So if your launchd job label is `com.apple.Mail.helper`, this must be the name of the tool in your application bundle.

## Parameters

- `domain`: The job’s domain. The Service Management framework only supports the   domain.
- `executableLabel`: The label of the privileged executable to install. This label must be one of the keys found in the   dictionary in the application’s  .
- `auth`: An authorization reference containing the   right.
- `outError`: An output reference to a   describing the specific error encountered while submitting the executable tool; or,   if successful. It’s the responsibility of the application to release the error reference. This argument may be  .

## See Also

- [class SMAppService](smappservice.md)
  An object the framework uses to control helper executables that live inside an app’s main bundle.
- [Authorization Constants](authorization-constants.md)
  Constants that describe the ability to authorize helper executables or modify daemon applications.
- [Property List Keys](property-list-keys.md)
  Property list keys that describe the kinds of applications, daemons, and helper executables the framework manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smjobbless(_:_:_:_:))*