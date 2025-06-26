# AuthorizationStatus

**Framework**: FamilyControls  
**Kind**: enum

The status of your app’s authorization to provide parental controls.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Declaration

```swift
enum AuthorizationStatus
```

## Topics

### Determining the Status
- [AuthorizationStatus.notDetermined](authorizationstatus/notdetermined.md)
  The app hasn’t requested authorization.
- [AuthorizationStatus.denied](authorizationstatus/denied.md)
  The user, parent, or guardian denied the request for authorization.
- [AuthorizationStatus.approved](authorizationstatus/approved.md)
  The user, parent, or guardian approved the request for authorization.
### Accessing the Raw Value
- [var rawValue: Int](authorizationstatus/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [AuthorizationStatus.RawValue](authorizationstatus/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Debugging
- [var description: String](authorizationstatus/description.md)
  A nonlocalized description of the authorization value, suitable for debugging.
### Comparing Status Instances
- [static func != (Self, Self) -> Bool](authorizationstatus/!=(_:_:).md)
  Returns a Boolean value that indicates whether two authorization statuses aren’t equal.
- [var hashValue: Int](authorizationstatus/hashvalue.md)
  The hashed value of the authorization status.
- [func hash(into: inout Hasher)](authorizationstatus/hash(into:).md)
  Hashes the essential components of the authorization status by feeding them into the given hash function.
### Encoding Status Instances
- [func encode(to: any Encoder) throws](authorizationstatus/encode(to:).md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int`.
### Creating Status
- [init(from: any Decoder) throws](authorizationstatus/init(from:).md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int`.
- [init?(rawValue: Int)](authorizationstatus/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Default Implementations
- [Equatable Implementations](authorizationstatus/equatable-implementations.md)
- [RawRepresentable Implementations](authorizationstatus/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [class AuthorizationCenter](authorizationcenter.md)
  The center for requesting authorization to provide parental controls.
- [Family Controls](../BundleResources/Entitlements/com.apple.developer.family-controls.md)
  A Boolean value that indicates whether the app can request or revoke authorization to provide parental controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/authorizationstatus)*