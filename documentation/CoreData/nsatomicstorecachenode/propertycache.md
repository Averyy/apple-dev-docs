# propertyCache

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The property cache dictionary of the node.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var propertyCache: NSMutableDictionary? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSMutableDictionary<NSString *,id> * propertyCache;
```

## Discussion

This dictionary is used by [`value(forKey:)`](./value%28forkey%29.md) and [`setValue(_:forKey:)`](./setvalue%28_,forkey%29.md) for property values. This property is `nil` unless it has been explicitly set or non-`nil` values have been set for keys using [`setValue(_:forKey:)`](./setvalue%28_,forkey%29.md).

## See Also

### Managing Node Data
- [var objectID: NSManagedObjectID](./objectid.md)
  The managed object ID of the node.
- [func value(forKey: String) -> Any?](./value%28forkey%29.md)
  Returns the value for a given key.
- [func setValue(Any?, forKey: String)](./setvalue%28_,forkey%29.md)
  Sets the value for the given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstorecachenode/propertycache)*