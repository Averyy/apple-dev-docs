# MPMediaEntityPersistentID

**Framework**: Media Player  
**Kind**: typealias  
**Role**: Type Alias

Defines the type for storing a persistent identifier to a particular entity.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias MPMediaEntityPersistentID = UInt64
```

```c
typedef uint64_t MPMediaEntityPersistentID;
```

#### Discussion

The value persists across application launches and across syncs that don’t change the sync status of the media item. The value isn’t guaranteed to persist across a sync/unsync/sync cycle.

## See Also

### Working with media properties
- [class func canFilter(byProperty: String) -> Bool](./mpmediaentity/canfilter%28byproperty%29.md)
  Indicates whether you can use the media property key that you specify to construct a media property predicate.
- [func enumerateValues(forProperties: Set<String>, using: (String, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](./mpmediaentity/enumeratevalues%28forproperties,using%29.md)
  Executes a provided block with the fetched values for the given item properties.
- [var persistentID: MPMediaEntityPersistentID](./mpmediaentity/persistentid.md)
  The persistent identifier for a media entity.
- [subscript(Any) -> Any?](./mpmediaentity/subscript%28_%29.md)
  Returns the object specified by the key.
- [func value(forProperty: String) -> Any?](./mpmediaentity/value%28forproperty%29.md)
  Retrieves the value for a specified media property key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaentitypersistentid)*