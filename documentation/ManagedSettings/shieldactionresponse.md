# ShieldActionResponse

**Framework**: ManagedSettings  
**Kind**: enum

Constants your extension that handles shield actions can use to tell the system how to respond to an action.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
enum ShieldActionResponse
```

## Topics

### Responses
- [ShieldActionResponse.close](shieldactionresponse/close.md)
  An instruction for the system to close the current application or web browser.
- [ShieldActionResponse.defer](shieldactionresponse/defer.md)
  An instruction to defer a response to the action.
- [ShieldActionResponse.none](shieldactionresponse/none.md)
  An instruction that the system doesn’t need to take any additional action on behalf of the extension.
### Comparisons
- [static func != (Self, Self) -> Bool](shieldactionresponse/!=(_:_:).md)
  Returns a Boolean value that indicates whether two values aren’t equal.
- [var hashValue: Int](shieldactionresponse/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](shieldactionresponse/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Initializers
- [init?(rawValue: Int)](shieldactionresponse/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: Int](shieldactionresponse/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [ShieldActionResponse.RawValue](shieldactionresponse/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](shieldactionresponse/equatable-implementations.md)
- [RawRepresentable Implementations](shieldactionresponse/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [enum ShieldAction](shieldaction.md)
  Constants that describe a user’s action for your extension to handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldactionresponse)*