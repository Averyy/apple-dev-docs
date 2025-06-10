# attribute(forKey:)

**Framework**: SceneKit  
**Kind**: method

Returns the value of a lighting attribute.

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

The value of the lighting attribute, or `nil` if no such attribute exists.

#### Discussion

A light’s [`type`](scnlight/type.md) property determines its set of available attributes.

You can also get the values of lighting attributes using [`Key-value coding`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KeyValueCoding.html#//apple_ref/doc/uid/TP40008195-CH25). The key path for each lighting attribute is listed in [`Lighting Attribute Keys`](lighting-attribute-keys.md).

## Parameters

- `key`: A constant specifying a lighting attribute. See   for available keys and their possible values.

## See Also

- [var name: String?](scnlight/name.md)
  A name associated with the light.
- [func setAttribute(Any?, forKey: String)](scnlight/setattribute(_:forkey:).md)
  Sets the value for a lighting attribute.
- [Lighting Attribute Keys](lighting-attribute-keys.md)
  Keys for specifying the behavior of a light using the [`attribute(forKey:)`](scnlight/attribute(forkey:).md) and [`setAttribute(_:forKey:)`](scnlight/setattribute(_:forkey:).md) methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/attribute(forkey:))*