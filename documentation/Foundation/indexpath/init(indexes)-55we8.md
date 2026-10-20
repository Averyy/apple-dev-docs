# init(indexes:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates an index path from a sequence of integers.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init<ElementSequence>(indexes: ElementSequence) where ElementSequence : Sequence, ElementSequence.Element == Int
```

## See Also

### Creating Index Paths
- [init()](./init%28%29.md)
  Creates an empty index path.
- [init(index: IndexPath.Element)](./init%28index%29.md)
  Creates an index path with a single element.
- [init(arrayLiteral: IndexPath.Element...)](./init%28arrayliteral%29.md)
  Creates an index path from an array literal.
- [init(indexes: Array<IndexPath.Element>)](./init%28indexes%29-7auqk.md)
  Creates an index path from an array of elements.
- [IndexPath.Element](./element.md)
  A type that represents one node of an index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/indexpath/init(indexes:)-55we8)*