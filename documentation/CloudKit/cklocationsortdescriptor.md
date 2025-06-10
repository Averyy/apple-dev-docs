# CKLocationSortDescriptor

**Framework**: CloudKit  
**Kind**: class

An object for sorting records that contain location data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class CKLocationSortDescriptor
```

#### Overview

You can add a location sort descriptor to your queries when searching for records. At creation time, you must provide the sort descriptor with a key that has a doc://com.apple.documentation/documentation/corelocation/cllocation object as its value. The sort descriptor uses the value of that key to perform the sort.

CloudKit computes distance by drawing a direct line between the two locations that follows the curvature of the Earth. Distances don’t account for altitude changes between the two locations.

## Topics

### Creating a Location Sort Descriptor
- [init(key: String, relativeLocation: CLLocation)](cklocationsortdescriptor/init(key:relativelocation:).md)
  Creates a location sort descriptor using the specified key and relative location.
- [init(coder: NSCoder)](cklocationsortdescriptor/init(coder:).md)
  Creates a location sort descriptor from a serialized instance.
### Accessing the Location Value
- [var relativeLocation: CLLocation](cklocationsortdescriptor/relativelocation.md)
  The reference location for sorting records.

## Relationships

### Inherits From
- [NSSortDescriptor](../Foundation/NSSortDescriptor.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CKQuery](ckquery.md)
  A query that describes the criteria to apply when searching for records in a database.
- [class CKQueryOperation](ckqueryoperation.md)
  An operation for executing queries in a database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cklocationsortdescriptor)*