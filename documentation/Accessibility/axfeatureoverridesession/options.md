# AXFeatureOverrideSession.Options

**Framework**: Accessibility  
**Kind**: struct  
**Role**: Structure

Options indicating which Accessibility features will be turned on or off when an override session is held by your app.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
struct Options
```

```c
enum AXFeatureOverrideSessionOptions : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./options/init%28rawvalue%29.md)
### Type Properties
- [static var grayscale: AXFeatureOverrideSession.Options](./options/grayscale.md)
- [static var invertColors: AXFeatureOverrideSession.Options](./options/invertcolors.md)
- [static var voiceControl: AXFeatureOverrideSession.Options](./options/voicecontrol.md)
- [static var voiceOver: AXFeatureOverrideSession.Options](./options/voiceover.md)
- [static var zoom: AXFeatureOverrideSession.Options](./options/zoom.md)

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

### Override sessions
- [class AXFeatureOverrideSession](../axfeatureoverridesession.md)
  A token object that represents an override session held by your app.
- [class AXFeatureOverrideSessionManager](../axfeatureoverridesessionmanager.md)
  A manager class to begin and end accessibility feature override sessions. Multiple override sessions are reconciled by combining the requests, preferring feature enablement. Ending all sessions restores the prior state of Accessibility feature enablement. Your app must be entitled with com.apple.developer.accessibility.merchant-api-control.
- [let AXFeatureOverrideSessionErrorDomain: String](../axfeatureoverridesessionerrordomain.md)
- [struct AXFeatureOverrideSessionError](../axfeatureoverridesessionerror-swift.struct.md)
- [AXFeatureOverrideSessionError.Code](../axfeatureoverridesessionerror-swift.struct/code.md)
- [com.apple.developer.accessibility.merchant-api-control](../../BundleResources/entitlements/com.apple.developer.accessibility.merchant-api-control.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axfeatureoverridesession/options)*