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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axfeatureoverridesessionmanager)*