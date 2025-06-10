# StringComparisonOperator

**Framework**: App Intents  
**Kind**: enum

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
enum StringComparisonOperator
```

## Topics

### Operators
- [static func == (StringComparisonOperator, StringComparisonOperator) -> Bool](stringcomparisonoperator/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [StringComparisonOperator.contains](stringcomparisonoperator/contains.md)
- [StringComparisonOperator.doesNotContain](stringcomparisonoperator/doesnotcontain.md)
- [StringComparisonOperator.hasPrefix](stringcomparisonoperator/hasprefix.md)
- [StringComparisonOperator.hasSuffix](stringcomparisonoperator/hassuffix.md)
### Instance Properties
- [var hashValue: Int](stringcomparisonoperator/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](stringcomparisonoperator/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](stringcomparisonoperator/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class HasPrefixComparator](hasprefixcomparator.md)
  An object that determines whether the value of a string property has the specified prefix.
- [class HasSuffixComparator](hassuffixcomparator.md)
  An object that determines whether the value of a string property has the specified suffix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/stringcomparisonoperator)*