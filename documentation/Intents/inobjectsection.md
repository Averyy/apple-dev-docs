# INObjectSection

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
class INObjectSection<ObjectType> where ObjectType : AnyObject
```

```objc
@interface INObjectSection : NSObject
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./inobjectsection/init%28coder%29.md)
- [init(title: String?, items: [ObjectType])](./inobjectsection/init%28title,items%29.md)
### Instance Properties
- [var items: [ObjectType]](./inobjectsection/items.md)
- [var title: String?](./inobjectsection/title.md)

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
- [class INObjectCollection](./inobjectcollection.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inobjectsection)*