# entries(passingTest:)

**Framework**: SceneKit  
**Kind**: method

Loads and returns all objects in the scene source that pass the test in a given block.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func entries(passingTest predicate: (Any, String, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [Any]
```

#### Return Value

An array of SceneKit objects from the scene source that pass the test.

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

Use this method to selectively load objects from a scene source matching criteria you specify. For example, the following code loads from a scene file only the nodes that have attached geometry:

```objc
NSArray *geometryNodes = [sceneSource entriesPassingTest:^BOOL(id entry, NSString *identifier, BOOL *stop) {
    if ([entry isKindOfClass:[SCNNode class]]) {
        SCNNode *node = (SCNNode *)entry;
        return (node.geometry != nil);
    } else {
        return NO;
    }
}];
```

## Parameters

- `predicate`: The block returns a Boolean value indicating whether the entry object passed the test and should be included in the method’s returned array.

## See Also

- [func identifiersOfEntries(withClass: AnyClass) -> [String]](scnscenesource/identifiersofentries(withclass:).md)
  Returns the identifiers for all objects in the scene source of the specified class.
- [func entryWithIdentifier<T>(String, withClass: T.Type) -> T?](scnscenesource/entrywithidentifier(_:withclass:).md)
  Loads and returns a specific object in the scene source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/entries(passingtest:))*