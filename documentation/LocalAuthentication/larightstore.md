# LARightStore

**Framework**: Local Authentication  
**Kind**: class

A container for data protected by a right.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class LARightStore
```

#### Overview

Use an [`LARightStore`](larightstore.md) along with an [`LARight`](laright.md) to make secrets accessible only after certain conditions, including authentication, are met. Storing secrets this way lets you tie the availability of sensitive resources to the authorization status of the user.

The following stores a named access token behind the default authorization requirements:

```swift
func storeBackendAccessToken(_ token: Data) async throws {
    let loginRight = LARight()
    _ = try await LARightStore.shared.saveRight(loginRight, identifier: "access-token", secret: token)
}
```

The system stores your secret in the keychain and protects it with a unique key in the Secure Enclave. The system associates the key with your right and with an access control list that ensures that the data is only accessible after your access requirements are met.

You can retrieve stored secrets later using the right’s identifier:

```swift
func fetchBackendAccessToken() async throws -> Data {
    let loginRight = try await LARightStore.shared.right(forIdentifier: "access-token")

    // Authorize the right or else the secret is unavailable.
    try await loginRight.authorize(localizedReason: "Access sandcastle competition server")
    return try await loginRight.secret.rawData
}
```

## Topics

### Accessing rights
- [class var shared: LARightStore](larightstore/shared.md)
  A shared object that stores rights.
- [func right(forIdentifier: String, completion: (LAPersistedRight?, (any Error)?) -> Void)](larightstore/right(foridentifier:completion:).md)
  Fetches a previously stored right from the shared right store.
### Storing rights
- [func saveRight(LARight, identifier: String, completion: (LAPersistedRight?, (any Error)?) -> Void)](larightstore/saveright(_:identifier:completion:).md)
  Saves a right to a persistent right store.
- [func saveRight(LARight, identifier: String, secret: Data, completion: (LAPersistedRight?, (any Error)?) -> Void)](larightstore/saveright(_:identifier:secret:completion:).md)
  Saves a right to a persistent store along with secret data you supply.
### Removing stored rights
- [func removeRight(LAPersistedRight, completion: ((any Error)?) -> Void)](larightstore/removeright(_:completion:).md)
  Removes a right from the right store given an instance of that right.
- [func removeRight(forIdentifier: String, completion: ((any Error)?) -> Void)](larightstore/removeright(foridentifier:completion:).md)
  Removes a right from the right store given its unique identifier.
- [func removeAllRights(completion: ((any Error)?) -> Void)](larightstore/removeallrights(completion:).md)
  Removes all rights associated with this client from the right store.

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

- [class LAPersistedRight](lapersistedright.md)
  A right that gates access to a key and a secret.
- [class LASecret](lasecret.md)
  Data that’s protected by a persisted right.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/larightstore)*