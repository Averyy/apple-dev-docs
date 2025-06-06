# persistentID

**Framework**: Media Player  
**Kind**: property

The persistent identifier for a media entity.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var persistentID: MPMediaEntityPersistentID { get }
```

## See Also

- [class func canFilter(byProperty: String) -> Bool](mpmediaentity/canfilter(byproperty:).md)
  Indicates whether you can use the media property key that you specify to construct a media property predicate.
- [func enumerateValues(forProperties: Set<String>, using: (String, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](mpmediaentity/enumeratevalues(forproperties:using:).md)
  Executes a provided block with the fetched values for the given item properties.
- [subscript(Any) -> Any?](mpmediaentity/subscript(_:).md)
  Returns the object specified by the key.
- [func value(forProperty: String) -> Any?](mpmediaentity/value(forproperty:).md)
  Retrieves the value for a specified media property key.
- [typealias MPMediaEntityPersistentID](mpmediaentitypersistentid.md)
  Defines the type for storing a persistent identifier to a particular entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaentity/persistentid)*