# enumerateValues(forProperties:using:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) enumerateValuesForProperties:(NSSet<NSString *> *) properties usingBlock:(void (^)(NSString *property, id value, BOOL *stop)) block;
```

## Discussion

Use this method to get property values in a batch fashion. Anytime the app accesses more than one property, enumerating over a set of property keys is more efficient than fetching each individual property with [`value(forProperty:)`](./value%28forproperty%29.md).

To see which media property keys you can use with this method, refer to [Media entity property keys](../media-entity-property-keys.md), [General media item property keys](../general-media-item-property-keys.md), [Playlist property keys](../playlist-property-keys.md), and [User-defined property keys](../user-defined-property-keys.md).

## Parameters

- `properties`: A set of property keys that you want the values for.
- `block`: A block object that executes for each fetched property value.

## See Also

### Working with media properties
- [class func canFilter(byProperty: String) -> Bool](./canfilter%28byproperty%29.md)
  Indicates whether you can use the media property key that you specify to construct a media property predicate.
- [var persistentID: MPMediaEntityPersistentID](./persistentid.md)
  The persistent identifier for a media entity.
- [subscript(Any) -> Any?](./subscript%28_%29.md)
  Returns the object specified by the key.
- [func value(forProperty: String) -> Any?](./value%28forproperty%29.md)
  Retrieves the value for a specified media property key.
- [typealias MPMediaEntityPersistentID](../mpmediaentitypersistentid.md)
  Defines the type for storing a persistent identifier to a particular entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaentity/enumeratevalues(forproperties:using:))*