# AXFeatureOverrideSessionManager

**Framework**: Accessibility  
**Kind**: class  
**Role**: Class

A manager class to begin and end accessibility feature override sessions. Multiple override sessions are reconciled by combining the requests, preferring feature enablement. Ending all sessions restores the prior state of Accessibility feature enablement. Your app must be entitled with com.apple.developer.accessibility.merchant-api-control.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
class AXFeatureOverrideSessionManager
```

```objc
@interface AXFeatureOverrideSessionManager : NSObject
```

## Topics

### Instance Methods
- [func beginOverrideSession(enabling: AXFeatureOverrideSession.Options, disabling: AXFeatureOverrideSession.Options) throws -> AXFeatureOverrideSession](./axfeatureoverridesessionmanager/beginoverridesession%28enabling,disabling%29.md)
- [func end(AXFeatureOverrideSession) throws](./axfeatureoverridesessionmanager/end%28_%29.md)
### Type Properties
- [class var sharedInstance: AXFeatureOverrideSessionManager](./axfeatureoverridesessionmanager/sharedinstance.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Override sessions
- [class AXFeatureOverrideSession](./axfeatureoverridesession.md)
  A token object that represents an override session held by your app.
- [AXFeatureOverrideSession.Options](./axfeatureoverridesession/options.md)
  Options indicating which Accessibility features will be turned on or off when an override session is held by your app.
- [let AXFeatureOverrideSessionErrorDomain: String](./axfeatureoverridesessionerrordomain.md)
- [struct AXFeatureOverrideSessionError](./axfeatureoverridesessionerror-swift.struct.md)
- [AXFeatureOverrideSessionError.Code](./axfeatureoverridesessionerror-swift.struct/code.md)
- [com.apple.developer.accessibility.merchant-api-control](../BundleResources/entitlements/com.apple.developer.accessibility.merchant-api-control.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axfeatureoverridesessionmanager)*