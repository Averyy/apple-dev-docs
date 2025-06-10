# MusicAuthorization.Status

**Framework**: MusicKit  
**Kind**: enum

A value that indicates the authorization status the user sets for the current app to access their Apple Music data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum Status
```

## Topics

### Enumeration Cases
- [MusicAuthorization.Status.authorized](musicauthorization/status/authorized.md)
  The user granted permission for the current app to use MusicKit.
- [MusicAuthorization.Status.denied](musicauthorization/status/denied.md)
  The user denied permission for the current app to use MusicKit.
- [MusicAuthorization.Status.notDetermined](musicauthorization/status/notdetermined.md)
  The user has yet to decide whether to authorize the current app to use MusicKit.
- [MusicAuthorization.Status.restricted](musicauthorization/status/restricted.md)
  Apps on this device can’t access MusicKit in a way that the user can’t change.
### Initializers
- [init?(rawValue: String)](musicauthorization/status/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: String](musicauthorization/status/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [MusicAuthorization.Status.RawValue](musicauthorization/status/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [CustomStringConvertible Implementations](musicauthorization/status/customstringconvertible-implementations.md)
- [Equatable Implementations](musicauthorization/status/equatable-implementations.md)
- [RawRepresentable Implementations](musicauthorization/status/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicauthorization/status)*