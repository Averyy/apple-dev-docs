# ASCredentialIdentityStoreState

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

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

```objc
@interface ASCredentialIdentityStoreState : NSObject
```

## Topics

### Checking the state
- [var isEnabled: Bool](./ascredentialidentitystorestate/isenabled.md)
  A Boolean value indicating whether the credential identity store is enabled.
- [var supportsIncrementalUpdates: Bool](./ascredentialidentitystorestate/supportsincrementalupdates.md)
  A Boolean value indicating whether the credential identity store supports incremental updates.

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

### Checking the state of the store
- [func getState((ASCredentialIdentityStoreState) -> Void)](./ascredentialidentitystore/getstate%28_%29.md)
  Gets the state of the credential identity store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystorestate)*