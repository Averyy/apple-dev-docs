# NSWorkspace.LaunchConfigurationKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

The following keys can be used in the configuration dictionary of the [`launchApplication(at:options:configuration:)`](./launchapplication%28at,options,configuration%29.md) method.  Each key is optional, and if omitted, default behavior is applied.

**Availability**:
- macOS 10.6+ - Deprecated in 11.0

> **Deprecated**: Use [`NSWorkspace.OpenConfiguration`](./openconfiguration.md) instead.

## Declaration

```swift
struct LaunchConfigurationKey
```

```c
typedef NSString * NSWorkspaceLaunchConfigurationKey;
```

## Topics

### Type Properties
- [static let appleEvent: NSWorkspace.LaunchConfigurationKey](./launchconfigurationkey/appleevent.md)
  The value is the first NSAppleEventDescriptor to send to the new app.  If an instance of the app is already running, this is sent to that app.
- [static let architecture: NSWorkspace.LaunchConfigurationKey](./launchconfigurationkey/architecture.md)
  The value is an NSNumber containing an Mach-O Architecture constant.  Ignored if a new instance of the app is not launched.
- [static let arguments: NSWorkspace.LaunchConfigurationKey](./launchconfigurationkey/arguments.md)
  The value is an `NSArray` of `NSStrings`, passed to the new app in the `argv` parameter.  Ignored if a new instance of the app is not launched. This constant is not available to sandboxed apps.
- [static let environment: NSWorkspace.LaunchConfigurationKey](./launchconfigurationkey/environment.md)
  The value is an `NSDictionary`, mapping `NSStrings` to `NSStrings`, containing environment variables to set for the new app.  Ignored if a new instance of the app is not launched. This constant is not available to sandboxed apps.
### Initializers
- [init(rawValue: String)](./launchconfigurationkey/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Deprecated types
- [NSWorkspace.LaunchOptions](./launchoptions.md)
  Constants specifying how you want to launch an app
- [NSWorkspace.FileOperationName](./fileoperationname.md)
  Constants that define types of file operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/launchconfigurationkey)*