# enumerateValues(forProperties:using:)

**Framework**: Media Player  
**Kind**: method

Executes a provided block with the fetched values for the given item properties.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func enumerateValues(forProperties properties: Set<String>, using block: @escaping (String, Any, UnsafeMutablePointer<ObjCBool>) -> Void)
```

#### Discussion

Use this method to get property values in a batch fashion. Anytime the app accesses more than one property, enumerating over a set of property keys is more efficient than fetching each individual property with [`value(forProperty:)`](mpmediaentity/value(forproperty:).md).

To see which media property keys you can use with this method, refer to [`Media entity property keys`](media-entity-property-keys.md), [`General media item property keys`](general-media-item-property-keys.md), [`Playlist property keys`](playlist-property-keys.md), and [`User-defined property keys`](user-defined-property-keys.md).

## Parameters

- `properties`: A set of property keys that you want the values for.
- `block`: A block object that executes for each fetched property value.

## See Also

- [class func canFilter(byProperty: String) -> Bool](mpmediaentity/canfilter(byproperty:).md)
  Indicates whether you can use the media property key that you specify to construct a media property predicate.
- [var persistentID: MPMediaEntityPersistentID](mpmediaentity/persistentid.md)
  The persistent identifier for a media entity.
- [subscript(Any) -> Any?](mpmediaentity/subscript(_:).md)
  Returns the object specified by the key.
- [func value(forProperty: String) -> Any?](mpmediaentity/value(forproperty:).md)
  Retrieves the value for a specified media property key.
- [typealias MPMediaEntityPersistentID](mpmediaentitypersistentid.md)
  Defines the type for storing a persistent identifier to a particular entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaentity/enumeratevalues(forproperties:using:))*