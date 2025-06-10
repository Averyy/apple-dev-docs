# Platform

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

### Obtaining supported platforms
- [static var iOS: Platform](platform/ios.md)
  iOS is a supported platform.
- [static var macOS: Platform](platform/macos.md)
  macOS is a supported platform.
### Inspecting the object
- [var description: String](platform/description.md)
  A textual representation of this instance.
### Operators
- [static func == (Platform, Platform) -> Bool](platform/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](platform/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](platform/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static var visionOS: Platform](platform/visionos.md)
  visionOS is a supported platform.
### Default Implementations
- [Equatable Implementations](platform/equatable-implementations.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/platform)*