# INUserContext

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An object that provides user information to Siri.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INUserContext
```

```objc
@interface INUserContext : NSObject
```

## Topics

### Setting the User Context
- [func becomeCurrent()](./inusercontext/becomecurrent%28%29.md)
  Replaces the previous context object with the current context object that has the same underlying type.
### Initializers
- [init?(coder: NSCoder)](./inusercontext/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [INMediaUserContext](./inmediausercontext.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### User Context
- [class INMediaUserContext](./inmediausercontext.md)
  An object that provides user information to Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inusercontext)*