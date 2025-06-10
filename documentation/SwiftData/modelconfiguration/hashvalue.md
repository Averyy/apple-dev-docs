# hashValue

**Framework**: SwiftData  
**Kind**: property

The hash value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
var hashValue: Int { get }
```

#### Discussion

Hash values are not guaranteed to be equal across different executions of your program. Do not save hash values to use during a future execution.

> ❗ **Important**: `hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.

## See Also

- [func hash(into: inout Hasher)](modelconfiguration/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelconfiguration/hashvalue)*