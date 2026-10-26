# INObjectCollection

**Framework**: Intents  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class INObjectCollection<ObjectType> where ObjectType : AnyObject
```

```objc
@interface INObjectCollection : NSObject
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./inobjectcollection/init%28coder%29.md)
- [convenience init(items: [ObjectType])](./inobjectcollection/init%28items%29.md)
- [init(sections: [INObjectSection<ObjectType>])](./inobjectcollection/init%28sections%29.md)
### Instance Properties
- [var allItems: [ObjectType]](./inobjectcollection/allitems.md)
- [var sections: [INObjectSection<ObjectType>]](./inobjectcollection/sections.md)
- [var usesIndexedCollation: Bool](./inobjectcollection/usesindexedcollation.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Custom Objects
- [class INObject](./inobject.md)
  A representation of a custom intent parameter or response property.
- [class INObjectSection](./inobjectsection.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inobjectcollection)*