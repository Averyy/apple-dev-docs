# MeshBuffer

**Framework**: RealityKit  
**Kind**: struct

Mesh buffer containing elements of any type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct MeshBuffer<Element>
```

## Topics

### Creating a mesh buffer
- [init<S>(S)](meshbuffer/init(_:)-13uzl.md)
  Create a buffer from any sequence of elements.
- [init([Element])](meshbuffer/init(_:)-1f0ai.md)
  Create buffer from an array of elements.
- [init([Element])](meshbuffer/init(_:)-1hyiz.md)
  Create buffer from an array of elements.
- [init<S>(S)](meshbuffer/init(_:)-2okpc.md)
  Create a buffer from any sequence of elements.
- [init([Element])](meshbuffer/init(_:)-3bqai.md)
  Create buffer from an array of elements.
- [init<S>(S)](meshbuffer/init(_:)-3pbx9.md)
  Create a buffer from any sequence of elements.
- [init<S>(S)](meshbuffer/init(_:)-4ahf1.md)
  Create a buffer from any sequence of elements.
- [init<S>(S)](meshbuffer/init(_:)-5a11h.md)
  Create a buffer from any sequence of elements.
- [init([Element])](meshbuffer/init(_:)-5sh0b.md)
  Create buffer from an array of elements.
- [init([Element])](meshbuffer/init(_:)-650mf.md)
  Create buffer from an array of elements.
- [init<S>(S)](meshbuffer/init(_:)-6hldv.md)
  Create a buffer from any sequence of elements.
- [init([Element])](meshbuffer/init(_:)-77mou.md)
  Create buffer from an array of elements.
- [init<S>(S)](meshbuffer/init(_:)-7d6t8.md)
  Create a buffer from any sequence of elements.
- [init([Element])](meshbuffer/init(_:)-8m4zg.md)
  Create buffer from an array of elements.
- [init<S>(S)](meshbuffer/init(_:)-8p5ux.md)
  Create a buffer from any sequence of elements.
- [init<S>(S)](meshbuffer/init(_:)-8yhn7.md)
  Create a buffer from any sequence of elements.
- [init<S>(S)](meshbuffer/init(_:)-94e5y.md)
  Create a buffer from any sequence of elements.
- [init([Element])](meshbuffer/init(_:)-991gl.md)
  Create buffer from an array of elements.
- [init<S>(S)](meshbuffer/init(_:)-9eppl.md)
  Create a buffer from any sequence of elements.
- [init([Element])](meshbuffer/init(_:)-9o6sp.md)
  Create buffer from an array of elements.
- [init([Element])](meshbuffer/init(_:)-9tja8.md)
  Create buffer from an array of elements.
- [init([Element])](meshbuffer/init(_:)-11fcy.md)
  Create buffer from an array of elements.
- [init(elements: [Element], indices: [UInt32])](meshbuffer/init(elements:indices:)-2f47d.md)
  Create buffer from an array of element values and an array of indices into that value array.
- [init(elements: [Element], indices: [UInt32])](meshbuffer/init(elements:indices:)-2nr7l.md)
  Create buffer from an array of element values and an array of indices into that value array.
- [init(elements: [Element], indices: [UInt32])](meshbuffer/init(elements:indices:)-2wcfg.md)
  Create buffer from an array of element values and an array of indices into that value array.
- [init(elements: [Element], indices: [UInt32])](meshbuffer/init(elements:indices:)-3m3mo.md)
  Create buffer from an array of element values and an array of indices into that value array.
- [init(elements: [Element], indices: [UInt32])](meshbuffer/init(elements:indices:)-4kg29.md)
  Create buffer from an array of element values and an array of indices into that value array.
- [init(elements: [Element], indices: [UInt32])](meshbuffer/init(elements:indices:)-4yxh4.md)
  Create buffer from an array of element values and an array of indices into that value array.
- [init(elements: [Element], indices: [UInt32])](meshbuffer/init(elements:indices:)-5mhon.md)
  Create buffer from an array of element values and an array of indices into that value array.
- [init(elements: [Element], indices: [UInt32])](meshbuffer/init(elements:indices:)-76tes.md)
  Create buffer from an array of element values and an array of indices into that value array.
- [init(elements: [Element], indices: [UInt32])](meshbuffer/init(elements:indices:)-7gw7i.md)
  Create buffer from an array of element values and an array of indices into that value array.
- [init(elements: [Element], indices: [UInt32])](meshbuffer/init(elements:indices:)-8dbzg.md)
  Create buffer from an array of element values and an array of indices into that value array.
- [init(elements: [Element], indices: [UInt32])](meshbuffer/init(elements:indices:)-97yff.md)
  Create buffer from an array of element values and an array of indices into that value array.
### Inspecting a mesh
- [let count: Int](meshbuffer/count.md)
  The number of elements in the buffer.
- [var elements: [Element]](meshbuffer/elements.md)
  Access the buffer as an array. This may create a copy if the data are not already an array.
- [MeshBuffer.Element](meshbuffer/element.md)
  A type representing the sequence’s elements.
- [var rate: MeshBuffers.Rate](meshbuffer/rate.md)
  Rate of the buffer.
### Iterating the elements of a buffer
- [func makeIterator() -> MeshBuffer<Element>.Iterator](meshbuffer/makeiterator.md)
  Returns an iterator over the elements of this sequence.
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
### Initializers
- [init([Element])](meshbuffer/init(_:)-3v7qg.md)
  Create buffer from an array of elements.
- [init<S>(S)](meshbuffer/init(_:)-ig4m.md)
  Create a buffer from any sequence of elements.
- [init(elements: [Element], indices: [UInt32])](meshbuffer/init(elements:indices:)-2au73.md)
  Create buffer from an array of element values and an array of indices into that value array.
### Default Implementations
- [Sequence Implementations](meshbuffer/sequence-implementations.md)

## Relationships

### Conforms To
- [Sequence](../Swift/Sequence.md)

## See Also

- [protocol MeshBufferContainer](meshbuffercontainer.md)
  Conforming objects contain a table of mesh buffers.
- [protocol MeshBufferSemantic](meshbuffersemantic.md)
  A protocol that holds an identifier value for mesh buffers.
- [enum MeshBuffers](meshbuffers.md)
  An object that holds the data for an model entity’s mesh.
- [struct AnyMeshBuffer](anymeshbuffer.md)
  Mesh buffer stored in the container.
- [struct MeshInstanceCollection](meshinstancecollection.md)
  An object that holds a collection of mesh resource instances.
- [struct MeshModelCollection](meshmodelcollection.md)
  An object that holds a collection of mesh models.
- [struct MeshPartCollection](meshpartcollection.md)
  An object that holds a collection of mesh parts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshbuffer)*