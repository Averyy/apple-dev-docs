# MeshBuffer

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Mesh buffer containing elements of any type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct MeshBuffer<Element>
```

## Topics

### Creating a mesh buffer
- [init<S>(S)](./meshbuffer/init%28_%29-13uzl.md)
  Create a buffer from any sequence of elements.
- [init([Element])](./meshbuffer/init%28_%29-1f0ai.md)
  Create buffer from an array of elements.
- [init([Element])](./meshbuffer/init%28_%29-1hyiz.md)
  Create buffer from an array of elements.
- [init<S>(S)](./meshbuffer/init%28_%29-2okpc.md)
  Create a buffer from any sequence of elements.
- [init([Element])](./meshbuffer/init%28_%29-3bqai.md)
  Create buffer from an array of elements.
- [init<S>(S)](./meshbuffer/init%28_%29-3pbx9.md)
  Create a buffer from any sequence of elements.
- [init<S>(S)](./meshbuffer/init%28_%29-4ahf1.md)
  Create a buffer from any sequence of elements.
- [init<S>(S)](./meshbuffer/init%28_%29-5a11h.md)
  Create a buffer from any sequence of elements.
- [init([Element])](./meshbuffer/init%28_%29-5sh0b.md)
  Create buffer from an array of elements.
- [init([Element])](./meshbuffer/init%28_%29-650mf.md)
  Create buffer from an array of elements.
- [init<S>(S)](./meshbuffer/init%28_%29-6hldv.md)
  Create a buffer from any sequence of elements.
- [init([Element])](./meshbuffer/init%28_%29-77mou.md)
  Create buffer from an array of elements.
- [init<S>(S)](./meshbuffer/init%28_%29-7d6t8.md)
  Create a buffer from any sequence of elements.
- [init([Element])](./meshbuffer/init%28_%29-8m4zg.md)
  Create buffer from an array of elements.
- [init<S>(S)](./meshbuffer/init%28_%29-8p5ux.md)
  Create a buffer from any sequence of elements.
- [init<S>(S)](./meshbuffer/init%28_%29-8yhn7.md)
  Create a buffer from any sequence of elements.
- [init<S>(S)](./meshbuffer/init%28_%29-94e5y.md)
  Create a buffer from any sequence of elements.
- [init([Element])](./meshbuffer/init%28_%29-991gl.md)
  Create buffer from an array of elements.
- [init<S>(S)](./meshbuffer/init%28_%29-9eppl.md)
  Create a buffer from any sequence of elements.
- [init([Element])](./meshbuffer/init%28_%29-9o6sp.md)
  Create buffer from an array of elements.
- [init([Element])](./meshbuffer/init%28_%29-9tja8.md)
  Create buffer from an array of elements.
- [init([Element])](./meshbuffer/init%28_%29-11fcy.md)
  Create buffer from an array of elements.
- [init(elements: [Element], indices: [UInt32])](./meshbuffer/init%28elements,indices%29-2f47d.md)
  Create buffer from an array of element values and an array of indices into that value array.
- [init(elements: [Element], indices: [UInt32])](./meshbuffer/init%28elements,indices%29-2nr7l.md)
  Create buffer from an array of element values and an array of indices into that value array.
- [init(elements: [Element], indices: [UInt32])](./meshbuffer/init%28elements,indices%29-2wcfg.md)
  Create buffer from an array of element values and an array of indices into that value array.
- [init(elements: [Element], indices: [UInt32])](./meshbuffer/init%28elements,indices%29-3m3mo.md)
  Create buffer from an array of element values and an array of indices into that value array.
- [init(elements: [Element], indices: [UInt32])](./meshbuffer/init%28elements,indices%29-4kg29.md)
  Create buffer from an array of element values and an array of indices into that value array.
- [init(elements: [Element], indices: [UInt32])](./meshbuffer/init%28elements,indices%29-4yxh4.md)
  Create buffer from an array of element values and an array of indices into that value array.
- [init(elements: [Element], indices: [UInt32])](./meshbuffer/init%28elements,indices%29-5mhon.md)
  Create buffer from an array of element values and an array of indices into that value array.
- [init(elements: [Element], indices: [UInt32])](./meshbuffer/init%28elements,indices%29-76tes.md)
  Create buffer from an array of element values and an array of indices into that value array.
- [init(elements: [Element], indices: [UInt32])](./meshbuffer/init%28elements,indices%29-7gw7i.md)
  Create buffer from an array of element values and an array of indices into that value array.
- [init(elements: [Element], indices: [UInt32])](./meshbuffer/init%28elements,indices%29-8dbzg.md)
  Create buffer from an array of element values and an array of indices into that value array.
- [init(elements: [Element], indices: [UInt32])](./meshbuffer/init%28elements,indices%29-97yff.md)
  Create buffer from an array of element values and an array of indices into that value array.
### Inspecting a mesh
- [var elements: [Element]](./meshbuffer/elements.md)
  Access the buffer as an array. This may create a copy if the data are not already an array.
- [var rate: MeshBuffers.Rate](./meshbuffer/rate.md)
  Rate of the buffer.
### Iterating the elements of a buffer
- [func forEach((Element, Element) throws -> Void) rethrows](./meshbuffer/foreach%28_%29-53vhs.md)
  Iterate over pairs of elements.
- [func forEach((Element, Element, Element) throws -> Void) rethrows](./meshbuffer/foreach%28_%29-7o3tb.md)
  Iterate over three elements per step.
- [func forEach((Element, Element, Element, Element) throws -> Void) rethrows](./meshbuffer/foreach%28_%29-xhri.md)
  Iterate over four elements per step.
- [func usingRate(MeshBuffers.Rate) -> MeshBuffer<Element>](./meshbuffer/usingrate%28_%29.md)
  New object with updated rate.
### Initializers
- [init(_:)](./meshbuffer/init%28_%29.md)
  Create buffer from an array of elements.
- [init(elements:indices:)](./meshbuffer/init%28elements,indices%29.md)
  Create buffer from an array of element values and an array of indices into that value array.
### Instance Properties
- [let count: Int](./meshbuffer/count.md)
  The number of elements in the buffer.
### Instance Methods
- [func forEach(_:)](./meshbuffer/foreach%28_%29.md)
  Iterate over pairs of elements.

## Relationships

### Conforms To
- [Sequence](../Swift/sequence.md)

## See Also

### Mesh description
- [protocol MeshBufferContainer](./meshbuffercontainer.md)
  Conforming objects contain a table of mesh buffers.
- [protocol MeshBufferSemantic](./meshbuffersemantic.md)
  A protocol that holds an identifier value for mesh buffers.
- [enum MeshBuffers](./meshbuffers.md)
  An object that holds the data for an model entity’s mesh.
- [struct AnyMeshBuffer](./anymeshbuffer.md)
  Mesh buffer stored in the container.
- [struct MeshInstanceCollection](./meshinstancecollection.md)
  An object that holds a collection of mesh resource instances.
- [struct MeshModelCollection](./meshmodelcollection.md)
  An object that holds a collection of mesh models.
- [struct MeshPartCollection](./meshpartcollection.md)
  An object that holds a collection of mesh parts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshbuffer)*