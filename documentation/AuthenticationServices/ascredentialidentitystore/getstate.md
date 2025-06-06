# getState(_:)

**Framework**: Authentication Services  
**Kind**: method

Gets the state of the credential identity store.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func state() async -> ASCredentialIdentityStoreState
```

#### Discussion

Call this method to find out the current state of the store before attempting to call other store methods. Examine the [`ASCredentialIdentityStoreState`](ascredentialidentitystorestate.md) value passed to your completion handler to find out whether the store is enabled and whether it supports incremental updates.

## Parameters

- `completion`: A block the method calls to return the current identity store state.

## See Also

- [class ASCredentialIdentityStoreState](ascredentialidentitystorestate.md)
  A representation of the state of a credential identity store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystore/getstate(_:))*