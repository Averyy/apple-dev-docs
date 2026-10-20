# NSWorkspace.LaunchOptions

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants specifying how you want to launch an app

**Availability**:
- macOS

## Declaration

```swift
struct LaunchOptions
```

```c
enum NSWorkspaceLaunchOptions : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./launchoptions/init%28rawvalue%29.md)
### Deprecated
- [Deprecated symbols](../launchoptions-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Deprecated types
- [NSWorkspace.LaunchConfigurationKey](./launchconfigurationkey.md)
  The following keys can be used in the configuration dictionary of the [`launchApplication(at:options:configuration:)`](./launchapplication%28at,options,configuration%29.md) method.  Each key is optional, and if omitted, default behavior is applied.
- [NSWorkspace.FileOperationName](./fileoperationname.md)
  Constants that define types of file operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/launchoptions)*