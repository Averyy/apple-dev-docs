# setAttribute(_:forKey:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Sets a scene attribute for the specified key.

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
func setAttribute(_ attribute: Any?, forKey key: String)
```

```objc
- (void) setAttribute:(id) attribute forKey:(NSString *) key;
```

## Parameters

- `attribute`: An object that specifies the value of the attribute to be written.
- `key`: One of the constants described in [Scene Attributes](../scene-attributes.md) that identifies the attribute to be written.

## See Also

### Managing Scene Attributes
- [func attribute(forKey: String) -> Any?](./attribute%28forkey%29.md)
  Returns the scene attribute for the specified key.
- [SCNScene.Attribute](./attribute.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/setattribute(_:forkey:))*