# AXFeatureOverrideSession.Options

**Framework**: Accessibility  
**Kind**: struct

Options indicating which Accessibility features will be turned on or off when an override session is held by your app.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
struct Options
```

## Topics

### Initializers
- [init(rawValue: UInt)](axfeatureoverridesession/options/init(rawvalue:).md)
### Type Properties
- [static var grayscale: AXFeatureOverrideSession.Options](axfeatureoverridesession/options/grayscale.md)
- [static var invertColors: AXFeatureOverrideSession.Options](axfeatureoverridesession/options/invertcolors.md)
- [static var voiceControl: AXFeatureOverrideSession.Options](axfeatureoverridesession/options/voicecontrol.md)
- [static var voiceOver: AXFeatureOverrideSession.Options](axfeatureoverridesession/options/voiceover.md)
- [static var zoom: AXFeatureOverrideSession.Options](axfeatureoverridesession/options/zoom.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class AXFeatureOverrideSession](axfeatureoverridesession.md)
  A token object that represents an override session held by your app.
- [class AXFeatureOverrideSessionManager](axfeatureoverridesessionmanager.md)
  A manager class to begin and end accessibility feature override sessions. Multiple override sessions are reconciled by combining the requests, preferring feature enablement. Ending all sessions restores the prior state of Accessibility feature enablement. Your app must be entitled with com.apple.developer.accessibility.merchant-api-control.
- [let AXFeatureOverrideSessionErrorDomain: String](axfeatureoverridesessionerrordomain.md)
- [struct AXFeatureOverrideSessionError](axfeatureoverridesessionerror-swift.struct.md)
- [AXFeatureOverrideSessionError.Code](axfeatureoverridesessionerror-swift.struct/code.md)
- [com.apple.developer.accessibility.merchant-api-control](../BundleResources/Entitlements/com.apple.developer.accessibility.merchant-api-control.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axfeatureoverridesession/options)*