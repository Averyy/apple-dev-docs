# canFilter(byProperty:)

**Framework**: Media Player  
**Kind**: method

Indicates whether you can use the media property key that you specify to construct a media property predicate.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func canFilter(byProperty property: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the property you are testing can be used to construct a media property predicate of type [`MPMediaPropertyPredicate`](mpmediapropertypredicate.md); otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

To see which media property keys you can use with this method, refer to [`Media entity property keys`](media-entity-property-keys.md), [`General media item property keys`](general-media-item-property-keys.md), [`Playlist property keys`](playlist-property-keys.md), and [`User-defined property keys`](user-defined-property-keys.md).

## Parameters

- `property`: The key for the media property that you want to examine.

## See Also

- [func enumerateValues(forProperties: Set<String>, using: (String, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](mpmediaentity/enumeratevalues(forproperties:using:).md)
  Executes a provided block with the fetched values for the given item properties.
- [var persistentID: MPMediaEntityPersistentID](mpmediaentity/persistentid.md)
  The persistent identifier for a media entity.
- [subscript(Any) -> Any?](mpmediaentity/subscript(_:).md)
  Returns the object specified by the key.
- [func value(forProperty: String) -> Any?](mpmediaentity/value(forproperty:).md)
  Retrieves the value for a specified media property key.
- [typealias MPMediaEntityPersistentID](mpmediaentitypersistentid.md)
  Defines the type for storing a persistent identifier to a particular entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaentity/canfilter(byproperty:))*