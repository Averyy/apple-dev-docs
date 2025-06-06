# ShieldAction

**Framework**: ManagedSettings  
**Kind**: enum

Constants that describe a user’s action for your extension to handle.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
enum ShieldAction
```

## Topics

### Buttons
- [ShieldAction.primaryButtonPressed](shieldaction/primarybuttonpressed.md)
  The user pressed the top button of the buttons on a shield.
- [ShieldAction.secondaryButtonPressed](shieldaction/secondarybuttonpressed.md)
  The user pressed the optional secondary button underneath the primary button of a shield.
### Comparisons
- [static func != (Self, Self) -> Bool](shieldaction/!=(_:_:).md)
  Returns a Boolean value that indicates whether two values aren’t equal.
- [var hashValue: Int](shieldaction/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](shieldaction/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Initializers
- [init?(rawValue: Int)](shieldaction/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: Int](shieldaction/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [ShieldAction.RawValue](shieldaction/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](shieldaction/equatable-implementations.md)
- [RawRepresentable Implementations](shieldaction/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [enum ShieldActionResponse](shieldactionresponse.md)
  Constants your extension that handles shield actions can use to tell the system how to respond to an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldaction)*