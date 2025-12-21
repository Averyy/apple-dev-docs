# automaticTerminationSupportEnabled

**Framework**: Foundation  
**Kind**: property

A Boolean value indicating whether the app supports automatic termination.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var automaticTerminationSupportEnabled: Bool { get set }
```

#### Discussion

Without setting this property or setting the equivalent `Info.plist` key (`NSSupportsAutomaticTermination`), the methods [`disableAutomaticTermination(_:)`](processinfo/disableautomatictermination(_:).md) and [`enableAutomaticTermination(_:)`](processinfo/enableautomatictermination(_:).md) have no effect, although the counter tracking automatic termination opt-outs is still kept up to date to ensure correctness if this is called later. Currently, setting this property to [`false`](https://developer.apple.com/documentation/Swift/false) has no effect. This property should be set in the app delegate method [`applicationDidFinishLaunching(_:)`](https://developer.apple.com/documentation/AppKit/NSApplicationDelegate/applicationDidFinishLaunching(_:)) or earlier.

## See Also

- [func disableAutomaticTermination(String)](processinfo/disableautomatictermination(_:).md)
  Disables automatic termination for the application.
- [func enableAutomaticTermination(String)](processinfo/enableautomatictermination(_:).md)
  Enables automatic termination for the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/automaticterminationsupportenabled)*