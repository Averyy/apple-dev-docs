# attribute(forKey:)

**Framework**: SceneKit  
**Kind**: method

Returns the scene attribute for the specified key.

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