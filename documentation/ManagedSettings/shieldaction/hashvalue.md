# hashValue

**Framework**: ManagedSettings  
**Kind**: property

The hash value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var hashValue: Int { get }
```

#### Discussion

Hash values aren’t guaranteed to be equal across different executions of your program. Don’t save hash values to use during a future execution.

> ❗ **Important**: `hashValue` is deprecated as a [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable) requirement. To conform to Hashable, implement the [`hash(into:)`](shieldaction/hash(into:).md) requirement instead.

`hashValue` is deprecated as a [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable) requirement. To conform to Hashable, implement the [`hash(into:)`](shieldaction/hash(into:).md) requirement instead.

## See Also

- [static func != (Self, Self) -> Bool](shieldaction/!=(_:_:).md)
  Returns a Boolean value that indicates whether two values aren’t equal.
- [func hash(into: inout Hasher)](shieldaction/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldaction/hashvalue)*