# Mirror.DisplayStyle

**Framework**: Swift  
**Kind**: enum

A suggestion of how a mirror’s subject is to be interpreted.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum DisplayStyle
```

#### Overview

Playgrounds and the debugger will show a representation similar to the one used for instances of the kind indicated by the `DisplayStyle` case name when the mirror is used for display.

## Topics

### Operators
- [static func == (Mirror.DisplayStyle, Mirror.DisplayStyle) -> Bool](mirror/displaystyle-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [Mirror.DisplayStyle.class](mirror/displaystyle-swift.enum/class.md)
- [Mirror.DisplayStyle.collection](mirror/displaystyle-swift.enum/collection.md)
- [Mirror.DisplayStyle.dictionary](mirror/displaystyle-swift.enum/dictionary.md)
- [Mirror.DisplayStyle.enum](mirror/displaystyle-swift.enum/enum.md)
- [Mirror.DisplayStyle.optional](mirror/displaystyle-swift.enum/optional.md)
- [Mirror.DisplayStyle.set](mirror/displaystyle-swift.enum/set.md)
- [Mirror.DisplayStyle.struct](mirror/displaystyle-swift.enum/struct.md)
- [Mirror.DisplayStyle.tuple](mirror/displaystyle-swift.enum/tuple.md)
### Instance Properties
- [var hashValue: Int](mirror/displaystyle-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mirror/displaystyle-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mirror/displaystyle-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mirror/displaystyle-swift.enum)*