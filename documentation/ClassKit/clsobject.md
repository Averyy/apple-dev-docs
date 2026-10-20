# CLSObject

**Framework**: ClassKit  
**Kind**: class  
**Role**: Class

The abstract base class for objects managed by ClassKit.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CLSObject
```

```objc
@interface CLSObject : NSObject
```

## Topics

### Accessing Object Information
- [var dateCreated: Date](./clsobject/datecreated.md)
  The date on which the object was created.
- [var dateLastModified: Date](./clsobject/datelastmodified.md)
  The date on which the object was last modified.
### Initializers
- [init?(coder: NSCoder)](./clsobject/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CLSActivity](./clsactivity.md)
- [CLSActivityItem](./clsactivityitem.md)
- [CLSContext](./clscontext.md)
- [CLSProgressReportingCapability](./clsprogressreportingcapability.md)
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

### Creating contexts
- [init(type: CLSContextType, identifier: String, title: String)](./clscontext/init%28type,identifier,title%29.md)
  Initializes a new context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsobject)*