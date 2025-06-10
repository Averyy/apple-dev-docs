# environment

**Framework**: AppKit  
**Kind**: property

The value is an `NSDictionary`, mapping `NSStrings` to `NSStrings`, containing environment variables to set for the new app.  Ignored if a new instance of the app is not launched. This constant is not available to sandboxed apps.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static let environment: NSWorkspace.LaunchConfigurationKey
```

## See Also

- [static let appleEvent: NSWorkspace.LaunchConfigurationKey](nsworkspace/launchconfigurationkey/appleevent.md)
  The value is the first NSAppleEventDescriptor to send to the new app.  If an instance of the app is already running, this is sent to that app.
- [static let architecture: NSWorkspace.LaunchConfigurationKey](nsworkspace/launchconfigurationkey/architecture.md)
  The value is an NSNumber containing an Mach-O Architecture constant.  Ignored if a new instance of the app is not launched.
- [static let arguments: NSWorkspace.LaunchConfigurationKey](nsworkspace/launchconfigurationkey/arguments.md)
  The value is an `NSArray` of `NSStrings`, passed to the new app in the `argv` parameter.  Ignored if a new instance of the app is not launched. This constant is not available to sandboxed apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/launchconfigurationkey/environment)*