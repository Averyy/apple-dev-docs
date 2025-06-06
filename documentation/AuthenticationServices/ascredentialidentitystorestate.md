# ASCredentialIdentityStoreState

**Framework**: Authentication Services  
**Kind**: class

A representation of the state of a credential identity store.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class ASCredentialIdentityStoreState
```

## Topics

### Checking the state
- [var isEnabled: Bool](ascredentialidentitystorestate/isenabled.md)
  A Boolean value indicating whether the credential identity store is enabled.
- [var supportsIncrementalUpdates: Bool](ascredentialidentitystorestate/supportsincrementalupdates.md)
  A Boolean value indicating whether the credential identity store supports incremental updates.

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

- [func getState((ASCredentialIdentityStoreState) -> Void)](ascredentialidentitystore/getstate(_:).md)
  Gets the state of the credential identity store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystorestate)*