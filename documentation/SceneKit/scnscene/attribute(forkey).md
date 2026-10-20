# attribute(forKey:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Returns the scene attribute for the specified key.

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
func attribute(forKey key: String) -> Any?
```

```objc
- (id) attributeForKey:(NSString *) key;
```

#### Return Value

The scene attribute for the specified key, or `nil` if no such attribute exists.

## Parameters

- `key`: One of the constants described in [Scene Attributes](../scene-attributes.md) that identifies the attribute to be read.

## See Also

### Managing Scene Attributes
- [func setAttribute(Any?, forKey: String)](./setattribute%28_,forkey%29.md)
  Sets a scene attribute for the specified key.
- [SCNScene.Attribute](./attribute.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/attribute(forkey:))*