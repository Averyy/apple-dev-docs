# identifiersOfEntries(withClass:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Returns the identifiers for all objects in the scene source of the specified class.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
func identifiersOfEntries(withClass entryClass: AnyClass) -> [String]
```

```objc
- (NSArray<NSString *> *) identifiersOfEntriesWithClass:(Class) entryClass;
```

#### Return Value

An array of [`NSString`](../../Foundation/nsstring.md) objects, each the unique identifier of an object in the scene source.

#### Discussion

SceneKit recognizes objects of the following classes in scene files:

- [`CAAnimation`](../../QuartzCore/caanimation.md)
- [`NSImage`](../../AppKit/nsimage.md)
- [`SCNCamera`](../scncamera.md)
- [`SCNGeometry`](../scngeometry.md)
- [`SCNLight`](../scnlight.md)
- [`SCNMaterial`](../scnmaterial.md)
- [`SCNMorpher`](../scnmorpher.md)
- [`SCNNode`](../scnnode.md)
- [`SCNScene`](../scnscene.md)
- [`SCNSkinner`](../scnskinner.md)

Each object in a scene file has an identifier that is unique for its class. These identifiers are determined by the software that created the scene file—for example, they may be descriptive names assigned by an artist using 3D authoring tools. For SceneKit classes with a [`name`](../scnnode/name.md) property (such as nodes and geometries), the name of an object loaded from a scene file is based on its identifier in the scene file.

Use this method to enumerate all objects in a scene file of a specified class without loading the objects and their content. For example, the following code finds the identifiers for all animations stored in a scene source:

```objc
NSArray *animations = [sceneSource identifiersOfEntriesWithClass:[CAAnimation class]];
```

## Parameters

- `entryClass`: The class of objects to find identifiers for.

## See Also

### Loading and Inspecting Scene Elements
- [func entryWithIdentifier<T>(String, withClass: T.Type) -> T?](./entrywithidentifier%28_,withclass%29.md)
  Loads and returns a specific object in the scene source.
- [func entries(passingTest: (Any, String, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [Any]](./entries%28passingtest%29.md)
  Loads and returns all objects in the scene source that pass the test in a given block.
### Related Documentation
- [- entryWithIdentifier:withClass:](./entrywithidentifier_withclass_.md)
  Loads and returns a specific object in the scene source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/identifiersofentries(withclass:))*