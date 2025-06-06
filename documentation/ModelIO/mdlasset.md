# MDLAsset

**Framework**: Model I/O  
**Kind**: class

An indexed container for 3D objects and associated information, such as transform hierarchies, meshes, cameras, and lights.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLAsset
```

#### Overview

You create a [`MDLAsset`](mdlasset.md) object by loading data from a URL, and you can export an asset to any of several file formats. To access the objects contained in an asset, use [`Fast Enumeration`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Enumeration.html#//apple_ref/doc/uid/TP40008195-CH17-SW3), the [`object(at:)`](mdlasset/object(at:).md) method, or subscripting. Each object in an asset can be the root of a hierarchy of objects. To traverse that hierarchy, use an object’s [`children`](mdlobject/children.md) property.

An asset may contain timed information, such as a series of mesh morphs. In such cases, the asset’s [`frameInterval`](mdlasset/frameinterval.md) property is nonzero and the [`startTime`](mdlasset/starttime.md) and [`endTime`](mdlasset/endtime.md) properties indicate the range of sample times available in the asset data. For objects contained in the asset, you can use methods such as [`localTransform(atTime:)`](mdltransformcomponent/localtransform(attime:).md) and [`boundingBox(atTime:)`](mdlobject/boundingbox(attime:).md) to access object properties at a specific time sample. Requesting a sample outside the time range clamps to the start or end sample. Some asset formats support continuous sampling with interpolation for times between the samples stored in the asset; other asset formats are discrete. For an asset with discrete time information, requesting a sample time that falls between the samples stored in the asset returns data for the immediately preceding time.

## Topics

### Creating an Asset
- [class func canImportFileExtension(String) -> Bool](mdlasset/canimportfileextension(_:).md)
  Returns a Boolean value that indicates whether the [`MDLAsset`](mdlasset.md) class can read asset data from files with the specified extension.
- [init(url: URL)](mdlasset/init(url:).md)
  Initializes an asset from the file at the specified URL.
- [init(bufferAllocator: (any MDLMeshBufferAllocator)?)](mdlasset/init(bufferallocator:).md)
  Initializes an empty asset, using the specified buffer allocator.
- [init(url: URL?, vertexDescriptor: MDLVertexDescriptor?, bufferAllocator: (any MDLMeshBufferAllocator)?)](mdlasset/init(url:vertexdescriptor:bufferallocator:).md)
  Initializes an asset from the file at the specified URL, using the specified vertex descriptor and buffer allocator.
- [init(url: URL, vertexDescriptor: MDLVertexDescriptor?, bufferAllocator: (any MDLMeshBufferAllocator)?, preserveTopology: Bool, error: NSErrorPointer)](mdlasset/init(url:vertexdescriptor:bufferallocator:preservetopology:error:).md)
  Initializes an asset from the file at the specified URL, using the specified options for allocating and transforming data during import.
### Exporting an Asset
- [class func canExportFileExtension(String) -> Bool](mdlasset/canexportfileextension(_:).md)
  Returns a Boolean value that indicates whether the [`MDLAsset`](mdlasset.md) class can write asset data as a file with the specified format extension.
- [func export(to: URL) throws](mdlasset/export(to:).md)
  Writes asset data to a file at the specified URL and reports errors that occur during export.
### Working with Asset Content
- [func object(at: Int) -> MDLObject](mdlasset/object(at:).md)
  Returns the top-level object at the specified index in the asset.
- [subscript(Int) -> MDLObject?](mdlasset/subscript(_:).md)
  Returns the top-level object at the specified index in the asset, using subscript syntax.
- [var count: Int](mdlasset/count.md)
  The number of top-level objects in the asset.
- [func childObjects(of: AnyClass) -> [MDLObject]](mdlasset/childobjects(of:).md)
  Returns all objects contained in the asset of the specified class.
- [func add(MDLObject)](mdlasset/add(_:).md)
  Adds the specified object to the asset’s list of top-level objects.
- [func remove(MDLObject)](mdlasset/remove(_:).md)
  Removes the specified object from the asset’s list of top-level objects.
- [var boundingBox: MDLAxisAlignedBoundingBox](mdlasset/boundingbox.md)
  The minimum region entirely enclosing the asset’s contents.
- [func boundingBox(atTime: TimeInterval) -> MDLAxisAlignedBoundingBox](mdlasset/boundingbox(attime:).md)
  Returns the minimum region entirely enclosing the asset’s contents at the specified time sample.
- [var url: URL?](mdlasset/url.md)
  The URL from which the asset was loaded, if available.
- [var bufferAllocator: any MDLMeshBufferAllocator](mdlasset/bufferallocator.md)
  An object responsible for allocating mesh vertex data loaded from the asset.
- [var vertexDescriptor: MDLVertexDescriptor?](mdlasset/vertexdescriptor.md)
  The description of the vertex data format to be used for loading mesh data from the asset.
- [var masters: any MDLObjectContainerComponent](mdlasset/masters.md)
  An array of objects that can be reused in the asset’s object hierarchy through instancing.
### Working with Timed Information
- [var frameInterval: TimeInterval](mdlasset/frameinterval.md)
  The time interval between data samples in the asset.
- [var startTime: TimeInterval](mdlasset/starttime.md)
  The timestamp for the first timed data sample in the asset.
- [var endTime: TimeInterval](mdlasset/endtime.md)
  The timestamp for the last timed data sample in the asset.
### Working with Lights
- [class func placeLightProbes(withDensity: Float, heuristic: MDLProbePlacement, using: any MDLLightProbeIrradianceDataSource) -> [MDLLightProbe]](mdlasset/placelightprobes(withdensity:heuristic:using:).md)
  Automatically creates and places light probes for use in illuminating a scene.
- [enum MDLProbePlacement](mdlprobeplacement.md)
  Options affecting automatic placement of light probes in a scene, used with the [`placeLightProbes(withDensity:heuristic:using:)`](mdlasset/placelightprobes(withdensity:heuristic:using:).md) method.
### Constants
- [Asset File Types](asset-file-types.md)
  Uniform Type Identifiers for file formats supported by the Model I/O framework.
### Instance Properties
- [var animations: any MDLObjectContainerComponent](mdlasset/animations.md)
- [var originals: any MDLObjectContainerComponent](mdlasset/originals.md)
- [var resolver: (any MDLAssetResolver)?](mdlasset/resolver.md)
- [var upAxis: vector_float3](mdlasset/upaxis.md)
### Instance Methods
- [func loadTextures()](mdlasset/loadtextures.md)
- [func object(atPath: String) -> MDLObject](mdlasset/object(atpath:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSFastEnumeration](../Foundation/NSFastEnumeration.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MDLObject](mdlobject.md)
  The base class for objects that are part of a 3D asset, including meshes, cameras, and lights.
- [class MDLTransform](mdltransform.md)
  A description of the local coordinate space transformations for a 3D object.
- [class MDLMesh](mdlmesh.md)
  A container for vertex buffer data to be used in rendering a 3D object.
- [class MDLSubmesh](mdlsubmesh.md)
  A container for index buffer data and material information to be used in rendering all or part of a 3D object.
- [class MDLSubmeshTopology](mdlsubmeshtopology.md)
  A description of how a submesh’s index buffer data is arranged and how that arrangement should be used to produce the submesh’s intended 3D shape.
- [protocol MDLNamed](mdlnamed.md)
  The common interface for Model I/O objects that expose a human-readable name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlasset)*