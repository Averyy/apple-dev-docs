# name

**Framework**: SceneKit  
**Kind**: property

A name associated with the light.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var name: String? { get set }
```

#### Discussion

You can provide a descriptive name for a light to make managing your scene graph easier. Lights loaded from a scene file may have names assigned by an artist using a 3D authoring tool. To examine lights in a scene file without loading its scene graph, use the [`SCNSceneSource`](scnscenesource.md) class.

Light names are saved when you export a scene to a file using its [`write(to:options:delegate:progressHandler:)`](scnscene/write(to:options:delegate:progresshandler:).md) method. Light names also appear in the Xcode scene editor.

## See Also

- [func attribute(forKey: String) -> Any?](scnlight/attribute(forkey:).md)
  Returns the value of a lighting attribute.
- [func setAttribute(Any?, forKey: String)](scnlight/setattribute(_:forkey:).md)
  Sets the value for a lighting attribute.
- [Lighting Attribute Keys](lighting-attribute-keys.md)
  Keys for specifying the behavior of a light using the [`attribute(forKey:)`](scnlight/attribute(forkey:).md) and [`setAttribute(_:forKey:)`](scnlight/setattribute(_:forkey:).md) methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/name)*