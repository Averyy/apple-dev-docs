# subscript(_:)

**Framework**: Media Player  
**Kind**: subscript

Returns the object specified by the key.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
subscript(key: Any) -> Any? { get }
```

#### Return Value

The object that is specified by the key.

#### Discussion

The method provides read-only support for Objective-C subscripting syntax with [`MPMediaEntity`](mpmediaentity.md) property constants.

## Parameters

- `key`: The key associated with the retrieved object.

## See Also

- [class func canFilter(byProperty: String) -> Bool](mpmediaentity/canfilter(byproperty:).md)
  Indicates whether you can use the media property key that you specify to construct a media property predicate.
- [func enumerateValues(forProperties: Set<String>, using: (String, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](mpmediaentity/enumeratevalues(forproperties:using:).md)
  Executes a provided block with the fetched values for the given item properties.
- [var persistentID: MPMediaEntityPersistentID](mpmediaentity/persistentid.md)
  The persistent identifier for a media entity.
- [func value(forProperty: String) -> Any?](mpmediaentity/value(forproperty:).md)
  Retrieves the value for a specified media property key.
- [typealias MPMediaEntityPersistentID](mpmediaentitypersistentid.md)
  Defines the type for storing a persistent identifier to a particular entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaentity/subscript(_:))*