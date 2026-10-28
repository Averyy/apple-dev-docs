# setAttribute(_:forKey:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Sets the value for a lighting attribute.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

> **Deprecated**: Use properties instead. The property corresponding to each deprecated attribute is listed in [Lighting Attribute Keys](../lighting-attribute-keys.md).

## Declaration

```swift
func setAttribute(_ attribute: Any?, forKey key: String)
```

```objc
- (void) setAttribute:(id) attribute forKey:(NSString *) key;
```

## Discussion

A light’s [`type`](./type.md) property determines its set of available attributes.

You can also set or animate changes to the values of lighting attributes using [Key-value coding](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KeyValueCoding.html#//apple_ref/doc/uid/TP40008195-CH25). The key path for each lighting attribute is listed in [Lighting Attribute Keys](../lighting-attribute-keys.md).

## Parameters

- `attribute`: The value for the lighting attribute.
- `key`: A constant specifying a lighting attribute. See [Lighting Attribute Keys](../lighting-attribute-keys.md) for available keys and their possible values.

## See Also

### Managing Light Attributes
- [var name: String?](./name.md)
  A name associated with the light.
- [func attribute(forKey: String) -> Any?](./attribute%28forkey%29.md)
  Returns the value of a lighting attribute.
- [Lighting Attribute Keys](../lighting-attribute-keys.md)
  Keys for specifying the behavior of a light using the [`attribute(forKey:)`](./attribute%28forkey%29.md) and [`setAttribute(_:forKey:)`](./setattribute%28_,forkey%29.md) methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/setattribute(_:forkey:))*