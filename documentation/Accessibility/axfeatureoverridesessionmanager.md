# AXFeatureOverrideSessionManager

**Framework**: Accessibility  
**Kind**: class

A manager class to begin and end accessibility feature override sessions. Multiple override sessions are reconciled by combining the requests, preferring feature enablement. Ending all sessions restores the prior state of Accessibility feature enablement. Your app must be entitled with com.apple.developer.accessibility.merchant-api-control.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
class AXFeatureOverrideSessionManager
```

## Topics

### Instance Methods
- [func beginOverrideSession(enabling: AXFeatureOverrideSession.Options, disabling: AXFeatureOverrideSession.Options) throws -> AXFeatureOverrideSession](axfeatureoverridesessionmanager/beginoverridesession(enabling:disabling:).md)
- [func end(AXFeatureOverrideSession) throws](axfeatureoverridesessionmanager/end(_:).md)
### Type Properties
- [class var sharedInstance: AXFeatureOverrideSessionManager](axfeatureoverridesessionmanager/sharedinstance.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AXFeatureOverrideSession](axfeatureoverridesession.md)
  A token object that represents an override session held by your app.
- [AXFeatureOverrideSession.Options](axfeatureoverridesession/options.md)
  Options indicating which Accessibility features will be turned on or off when an override session is held by your app.
- [let AXFeatureOverrideSessionErrorDomain: String](axfeatureoverridesessionerrordomain.md)
- [struct AXFeatureOverrideSessionError](axfeatureoverridesessionerror-swift.struct.md)
- [AXFeatureOverrideSessionError.Code](axfeatureoverridesessionerror-swift.struct/code.md)
- [com.apple.developer.accessibility.merchant-api-control](../BundleResources/Entitlements/com.apple.developer.accessibility.merchant-api-control.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axfeatureoverridesessionmanager)*