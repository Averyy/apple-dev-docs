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

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CLSActivity](clsactivity.md)
- [CLSActivityItem](clsactivityitem.md)
- [CLSContext](clscontext.md)
- [CLSProgressReportingCapability](clsprogressreportingcapability.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [init(type: CLSContextType, identifier: String, title: String)](clscontext/init(type:identifier:title:).md)
  Initializes a new context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsobject)*