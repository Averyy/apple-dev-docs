# automaticTerminationSupportEnabled

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the app supports automatic termination.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var automaticTerminationSupportEnabled: Bool { get set }
```

```objc
@property BOOL automaticTerminationSupportEnabled;
```

## Discussion

Without setting this property or setting the equivalent `Info.plist` key (`NSSupportsAutomaticTermination`), the methods [`disableAutomaticTermination(_:)`](./disableautomatictermination%28_%29.md) and [`enableAutomaticTermination(_:)`](./enableautomatictermination%28_%29.md) have no effect, although the counter tracking automatic termination opt-outs is still kept up to date to ensure correctness if this is called later. Currently, setting this property to [`false`](../../Swift/false.md) has no effect. This property should be set in the app delegate method [`applicationDidFinishLaunching(_:)`](../../AppKit/nsapplicationdelegate/applicationdidfinishlaunching%28_%29.md) or earlier.

## See Also

### Controlling automatic termination
- [func disableAutomaticTermination(String)](./disableautomatictermination%28_%29.md)
  Disables automatic termination for the application.
- [func enableAutomaticTermination(String)](./enableautomatictermination%28_%29.md)
  Enables automatic termination for the application.
- [automaticTerminationOptOutCounter](../nsprocessinfo/automaticterminationoptoutcounter.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/automaticterminationsupportenabled)*