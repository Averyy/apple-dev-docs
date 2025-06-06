# ManagedApp.Platform

**Framework**: ManagedAppDistribution  
**Kind**: struct

The supported platform for the app.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- visionOS 2.4+

## Declaration

```swift
struct Platform
```

## Topics

### Operators
- [static func == (ManagedApp.Platform, ManagedApp.Platform) -> Bool](managedapp/platform-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var description: String](managedapp/platform-swift.struct/description.md)
  A textual representation of this instance.
- [var hashValue: Int](managedapp/platform-swift.struct/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](managedapp/platform-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static var iOS: ManagedApp.Platform](managedapp/platform-swift.struct/ios.md)
  iOS is a supported platform.
- [static var macOS: ManagedApp.Platform](managedapp/platform-swift.struct/macos.md)
  macOS is a supported platform.
- [static var visionOS: ManagedApp.Platform](managedapp/platform-swift.struct/visionos.md)
  visionOS is a supported platform.
### Default Implementations
- [Equatable Implementations](managedapp/platform-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let platform: Platform](managedapp/platform-swift.property.md)
  The platform of the app.
- [let requirements: String?](managedapp/requirements.md)
  The app’s localized operating system compatibility requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedapp/platform-swift.struct)*