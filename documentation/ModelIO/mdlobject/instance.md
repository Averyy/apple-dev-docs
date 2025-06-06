# instance

**Framework**: Model I/O  
**Kind**: property

The primary object, if applicable, of which this object is an instance.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var instance: MDLObject? { get set }
```

#### Discussion

Some asset formats supported by Model I/O provide , a feature where the asset provides a single definition for an object, then can reuse that definition at multiple points in a scene. For example, an asset describing a scene of a table and chairs could contain mesh and material data for only one chair, then use instancing to place several of the same chair around the table.

If an object loaded from an asset is an instance, this property refers to one of the objects in the asset’s [`masters`](mdlasset/masters.md) array. If this object is not an instance (or is loaded from an asset format that does not support instancing), this property is `nil`.

## See Also

- [var hidden: Bool](mdlobject/hidden.md)
  A Boolean value indicating whether this object should be used in rendering.
- [var path: String](mdlobject/path.md)
  A path that identifies the object in an asset’s object hierarchy using object names.
- [var components: [any MDLComponent]](mdlobject/components.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlobject/instance)*