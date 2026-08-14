# CLSObject

**Framework**: ClassKit  
**Kind**: class

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

## Topics

### Accessing Object Information
- [var dateCreated: Date](clsobject/datecreated.md)
  The date on which the object was created.
- [var dateLastModified: Date](clsobject/datelastmodified.md)
  The date on which the object was last modified.
### Initializers
- [init?(coder: NSCoder)](clsobject/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [CLSActivity](clsactivity.md)
- [CLSActivityItem](clsactivityitem.md)
- [CLSContext](clscontext.md)
- [CLSProgressReportingCapability](clsprogressreportingcapability.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [init(type: CLSContextType, identifier: String, title: String)](clscontext/init(type:identifier:title:).md)
  Initializes a new context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsobject)*