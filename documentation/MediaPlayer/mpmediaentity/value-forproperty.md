# value(forProperty:)

**Framework**: Media Player  
**Kind**: method

Retrieves the value for a specified media property key.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func value(forProperty property: String) -> Any?
```

#### Return Value

The value for the media `property` key.

#### Discussion

Use [`enumerateValues(forProperties:using:)`](mpmediaentity/enumeratevalues(forproperties:using:).md) to efficiently access more than one property at a time.

To see which media property keys you can use with this method, refer to [`Media entity property keys`](media-entity-property-keys.md), [`General media item property keys`](general-media-item-property-keys.md), [`Playlist property keys`](playlist-property-keys.md), and [`User-defined property keys`](user-defined-property-keys.md).

## Parameters

- `property`: The media property key that you want the corresponding value of.

## See Also

- [class func canFilter(byProperty: String) -> Bool](mpmediaentity/canfilter(byproperty:).md)
  Indicates whether you can use the media property key that you specify to construct a media property predicate.
- [func enumerateValues(forProperties: Set<String>, using: (String, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](mpmediaentity/enumeratevalues(forproperties:using:).md)
  Executes a provided block with the fetched values for the given item properties.
- [var persistentID: MPMediaEntityPersistentID](mpmediaentity/persistentid.md)
  The persistent identifier for a media entity.
- [subscript(Any) -> Any?](mpmediaentity/subscript(_:).md)
  Returns the object specified by the key.
- [typealias MPMediaEntityPersistentID](mpmediaentitypersistentid.md)
  Defines the type for storing a persistent identifier to a particular entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaentity/value(forproperty:))*