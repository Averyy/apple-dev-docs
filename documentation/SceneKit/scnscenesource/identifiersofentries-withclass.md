# identifiersOfEntries(withClass:)

**Framework**: SceneKit  
**Kind**: method

Returns the identifiers for all objects in the scene source of the specified class.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func identifiersOfEntries(withClass entryClass: AnyClass) -> [String]
```

#### Return Value

An array of [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects, each the unique identifier of an object in the scene source.

#### Discussion

SceneKit recognizes objects of the following classes in scene files:

- [`CAAnimation`](https://developer.apple.com/documentation/QuartzCore/CAAnimation)
- [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage)
- [`SCNCamera`](scncamera.md)
- [`SCNGeometry`](scngeometry.md)
- [`SCNLight`](scnlight.md)
- [`SCNMaterial`](scnmaterial.md)
- [`SCNMorpher`](scnmorpher.md)
- [`SCNNode`](scnnode.md)
- [`SCNScene`](scnscene.md)
- [`SCNSkinner`](scnskinner.md)

Each object in a scene file has an identifier that is unique for its class. These identifiers are determined by the software that created the scene file—for example, they may be descriptive names assigned by an artist using 3D authoring tools. For SceneKit classes with a [`name`](scnnode/name.md) property (such as nodes and geometries), the name of an object loaded from a scene file is based on its identifier in the scene file.

Use this method to enumerate all objects in a scene file of a specified class without loading the objects and their content. For example, the following code finds the identifiers for all animations stored in a scene source:

```objc
NSArray *animations = [sceneSource identifiersOfEntriesWithClass:[CAAnimation class]];
```

## Parameters

- `entryClass`: The class of objects to find identifiers for.

## See Also

- [func entryWithIdentifier<T>(String, withClass: T.Type) -> T?](scnscenesource/entrywithidentifier(_:withclass:).md)
  Loads and returns a specific object in the scene source.
- [func entries(passingTest: (Any, String, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [Any]](scnscenesource/entries(passingtest:).md)
  Loads and returns all objects in the scene source that pass the test in a given block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/identifiersofentries(withclass:))*