# attribute(forKey:)

**Framework**: SceneKit  
**Kind**: method

Returns the scene attribute for the specified key.

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
func attribute(forKey key: String) -> Any?
```

#### Return Value

The scene attribute for the specified key, or `nil` if no such attribute exists.

## Parameters

- `key`: One of the constants described in   that identifies the attribute to be read.

## See Also

- [func setAttribute(Any?, forKey: String)](scnscene/setattribute(_:forkey:).md)
  Sets a scene attribute for the specified key.
- [SCNScene.Attribute](scnscene/attribute.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/attribute(forkey:))*