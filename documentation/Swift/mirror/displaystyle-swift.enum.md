# Mirror.DisplayStyle

**Framework**: Swift  
**Kind**: enum  
**Role**: Enumeration

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
- [static func == (Mirror.DisplayStyle, Mirror.DisplayStyle) -> Bool](./displaystyle-swift.enum/eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [Mirror.DisplayStyle.class](./displaystyle-swift.enum/class.md)
- [Mirror.DisplayStyle.collection](./displaystyle-swift.enum/collection.md)
- [Mirror.DisplayStyle.dictionary](./displaystyle-swift.enum/dictionary.md)
- [Mirror.DisplayStyle.enum](./displaystyle-swift.enum/enum.md)
- [Mirror.DisplayStyle.foreignReference](./displaystyle-swift.enum/foreignreference.md)
- [Mirror.DisplayStyle.optional](./displaystyle-swift.enum/optional.md)
- [Mirror.DisplayStyle.set](./displaystyle-swift.enum/set.md)
- [Mirror.DisplayStyle.struct](./displaystyle-swift.enum/struct.md)
- [Mirror.DisplayStyle.tuple](./displaystyle-swift.enum/tuple.md)
### Instance Properties
- [var hashValue: Int](./displaystyle-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](./displaystyle-swift.enum/hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](./displaystyle-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../equatable.md)
- [Hashable](../hashable.md)
- [Sendable](../sendable.md)
- [SendableMetatype](../sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mirror/displaystyle-swift.enum)*