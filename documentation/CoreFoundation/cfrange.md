# CFRange

**Framework**: Core Foundation  
**Kind**: struct

A structure representing a range of sequential items in a container, such as characters in a buffer or elements in a collection.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct CFRange
```

## Topics

### Initializers
- [init()](cfrange/init.md)
- [init(location: CFIndex, length: CFIndex)](cfrange/init(location:length:).md)
### Instance Properties
- [var length: CFIndex](cfrange/length.md)
  An integer representing the number of items in the range. For type compatibility with the rest of the system, `LONG_MAX` is the maximum value you should use for length.
- [var location: CFIndex](cfrange/location.md)
  An integer representing the starting location of the range. For type compatibility with the rest of the system, `LONG_MAX` is the maximum value you should use for location.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias CFIndex](cfindex.md)
  Priority values used for kAXPriorityKey
- [typealias CFOptionFlags](cfoptionflags.md)
  A bitfield used for passing special allocation and other requests into Core Foundation functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrange)*