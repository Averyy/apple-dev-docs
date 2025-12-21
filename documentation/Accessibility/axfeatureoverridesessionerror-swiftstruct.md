# AXFeatureOverrideSessionError

**Framework**: Accessibility  
**Kind**: struct

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
struct AXFeatureOverrideSessionError
```

## Topics

### Type Properties
- [static var appNotEntitled: AXFeatureOverrideSessionError.Code](axfeatureoverridesessionerror-swift.struct/appnotentitled.md)
- [static var errorDomain: String](axfeatureoverridesessionerror-swift.struct/errordomain.md)
- [static var overrideIsAlreadyActive: AXFeatureOverrideSessionError.Code](axfeatureoverridesessionerror-swift.struct/overrideisalreadyactive.md)
- [static var overrideNotFoundForUUID: AXFeatureOverrideSessionError.Code](axfeatureoverridesessionerror-swift.struct/overridenotfoundforuuid.md)
- [static var undefined: AXFeatureOverrideSessionError.Code](axfeatureoverridesessionerror-swift.struct/undefined.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
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
- [AXFeatureOverrideSessionError.Code](axfeatureoverridesessionerror-swift.struct/code.md)
- [com.apple.developer.accessibility.merchant-api-control](../BundleResources/Entitlements/com.apple.developer.accessibility.merchant-api-control.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axfeatureoverridesessionerror-swift.struct)*