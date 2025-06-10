# String.StandardComparator

**Framework**: Swift  
**Kind**: struct

Compares `String`s using one of a fixed set of standard comparison algorithms.

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
struct StandardComparator
```

## Topics

### Initializers
- [init(String.StandardComparator, order: SortOrder)](string/standardcomparator/init(_:order:).md)
  Create a `StandardComparator` from the given `StandardComparator` with the given new `order`.
### Type Properties
- [static let lexical: String.StandardComparator](string/standardcomparator/lexical.md)
  Compares `String`s lexically.
- [static let localized: String.StandardComparator](string/standardcomparator/localized.md)
  Compares `String`s using a localized comparison in the current locale.
- [static let localizedStandard: String.StandardComparator](string/standardcomparator/localizedstandard.md)
  Compares `String`s as compared by the Finder.

## Relationships

### Conforms To
- [Decodable](decodable.md)
- [Encodable](encodable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [SortComparator](../Foundation/SortComparator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/standardcomparator)*