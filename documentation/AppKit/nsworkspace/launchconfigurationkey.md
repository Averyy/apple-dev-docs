# NSWorkspace.LaunchConfigurationKey

**Framework**: AppKit  
**Kind**: struct

The following keys can be used in the configuration dictionary of the [`launchApplication(at:options:configuration:)`](nsworkspace/launchapplication(at:options:configuration:).md) method.  Each key is optional, and if omitted, default behavior is applied.

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct LaunchConfigurationKey
```

## Topics

### Type Properties
- [static let appleEvent: NSWorkspace.LaunchConfigurationKey](nsworkspace/launchconfigurationkey/appleevent.md)
  The value is the first NSAppleEventDescriptor to send to the new app.  If an instance of the app is already running, this is sent to that app.
- [static let architecture: NSWorkspace.LaunchConfigurationKey](nsworkspace/launchconfigurationkey/architecture.md)
  The value is an NSNumber containing an Mach-O Architecture constant.  Ignored if a new instance of the app is not launched.
- [static let arguments: NSWorkspace.LaunchConfigurationKey](nsworkspace/launchconfigurationkey/arguments.md)
  The value is an `NSArray` of `NSStrings`, passed to the new app in the `argv` parameter.  Ignored if a new instance of the app is not launched. This constant is not available to sandboxed apps.
- [static let environment: NSWorkspace.LaunchConfigurationKey](nsworkspace/launchconfigurationkey/environment.md)
  The value is an `NSDictionary`, mapping `NSStrings` to `NSStrings`, containing environment variables to set for the new app.  Ignored if a new instance of the app is not launched. This constant is not available to sandboxed apps.
### Initializers
- [init(rawValue: String)](nsworkspace/launchconfigurationkey/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSWorkspace.LaunchOptions](nsworkspace/launchoptions.md)
  Constants specifying how you want to launch an app
- [NSWorkspace.FileOperationName](nsworkspace/fileoperationname.md)
  Constants that define types of file operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/launchconfigurationkey)*