# makeIterator()

**Framework**: RealityKit  
**Kind**: method

Returns an iterator over the elements of this sequence.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
func makeIterator() -> MeshBuffer<Element>.Iterator
```

## See Also

- [MeshBuffer.Iterator](meshbuffer/iterator.md)
  A type that provides the sequence’s iteration interface and encapsulates its iteration state.
- [func forEach((Element, Element) throws -> Void) rethrows](meshbuffer/foreach(_:)-53vhs.md)
  Iterate over pairs of elements.
- [func forEach((Element, Element, Element) throws -> Void) rethrows](meshbuffer/foreach(_:)-7o3tb.md)
  Iterate over three elements per step.
- [func forEach((Element, Element, Element, Element) throws -> Void) rethrows](meshbuffer/foreach(_:)-xhri.md)
  Iterate over four elements per step.
- [func usingRate(MeshBuffers.Rate) -> MeshBuffer<Element>](meshbuffer/usingrate(_:).md)
  New object with updated rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshbuffer/makeiterator())*