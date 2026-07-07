# UniqueBox

**Framework**: Swift  
**Kind**: struct

A smart pointer type that uniquely owns an instance of `Value` on the heap.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@frozen
struct UniqueBox<Value> where Value : ~Copyable
```

## Topics

### Initializers
- [init(consuming Value)](uniquebox/init(_:).md)
  Initializes a value of this unqiue box with the given initial value.
### Instance Properties
- [var mutableSpan: MutableSpan<Value>](uniquebox/mutablespan.md)
  A mutable span over the single element stored in this box.
- [var span: Span<Value>](uniquebox/span.md)
  A span over the single element stored in this box.
- [var value: Value](uniquebox/value.md)
  Dereferences the unique box allowing for in-place reads and writes to the stored `Value`.
### Instance Methods
- [func clone() -> UniqueBox<Value>](uniquebox/clone.md)
  Copies the value within the unqiue box and returns it in a new unique instance.
- [func consume() -> Value](uniquebox/consume.md)
  Consumes the unique box and returns the instance of `Value` that was within the box.

## Relationships

### Conforms To
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [struct UniqueArray](uniquearray.md)
  A dynamically self-resizing, heap allocated, noncopyable array of potentially noncopyable elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquebox)*