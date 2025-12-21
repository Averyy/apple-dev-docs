# AXFeatureOverrideSessionError.Code

**Framework**: Accessibility  
**Kind**: enum

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
enum Code
```

## Topics

### Enumeration Cases
- [AXFeatureOverrideSessionError.Code.appNotEntitled](axfeatureoverridesessionerror-swift.struct/code/appnotentitled.md)
- [AXFeatureOverrideSessionError.Code.overrideIsAlreadyActive](axfeatureoverridesessionerror-swift.struct/code/overrideisalreadyactive.md)
- [AXFeatureOverrideSessionError.Code.overrideNotFoundForUUID](axfeatureoverridesessionerror-swift.struct/code/overridenotfoundforuuid.md)
- [AXFeatureOverrideSessionError.Code.undefined](axfeatureoverridesessionerror-swift.struct/code/undefined.md)
### Initializers
- [init?(rawValue: Int)](axfeatureoverridesessionerror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AXFeatureOverrideSession](axfeatureoverridesession.md)
  A token object that represents an override session held by your app.
- [class AXFeatureOverrideSessionManager](axfeatureoverridesessionmanager.md)
  A manager class to begin and end accessibility feature override sessions. Multiple override sessions are reconciled by combining the requests, preferring feature enablement. Ending all sessions restores the prior state of Accessibility feature enablement. Your app must be entitled with com.apple.developer.accessibility.merchant-api-control.
- [AXFeatureOverrideSession.Options](axfeatureoverridesession/options.md)
  Options indicating which Accessibility features will be turned on or off when an override session is held by your app.
- [let AXFeatureOverrideSessionErrorDomain: String](axfeatureoverridesessionerrordomain.md)
- [struct AXFeatureOverrideSessionError](axfeatureoverridesessionerror-swift.struct.md)
- [com.apple.developer.accessibility.merchant-api-control](../BundleResources/Entitlements/com.apple.developer.accessibility.merchant-api-control.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axfeatureoverridesessionerror-swift.struct/code)*