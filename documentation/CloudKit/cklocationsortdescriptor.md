# CKLocationSortDescriptor

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

An object for sorting records that contain location data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class CKLocationSortDescriptor
```

```objc
@interface CKLocationSortDescriptor : NSSortDescriptor
```

#### Overview

You can add a location sort descriptor to your queries when searching for records. At creation time, you must provide the sort descriptor with a key that has a [`CLLocation`](../CoreLocation/cllocation.md) object as its value. The sort descriptor uses the value of that key to perform the sort.

CloudKit computes distance by drawing a direct line between the two locations that follows the curvature of the Earth. Distances don’t account for altitude changes between the two locations.

## Topics

### Creating a Location Sort Descriptor
- [init(key: String, relativeLocation: CLLocation)](./cklocationsortdescriptor/init%28key,relativelocation%29.md)
  Creates a location sort descriptor using the specified key and relative location.
- [init(coder: NSCoder)](./cklocationsortdescriptor/init%28coder%29.md)
  Creates a location sort descriptor from a serialized instance.
### Accessing the Location Value
- [var relativeLocation: CLLocation](./cklocationsortdescriptor/relativelocation.md)
  The reference location for sorting records.
### Initializers
- [convenience init(key: String?, ascending: Bool, comparator: Comparator)](./cklocationsortdescriptor/init%28key,ascending,comparator%29.md)

## Relationships

### Inherits From
- [NSSortDescriptor](../Foundation/nssortdescriptor.md)
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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Queries
- [class CKQuery](./ckquery.md)
  A query that describes the criteria to apply when searching for records in a database.
- [class CKQueryOperation](./ckqueryoperation.md)
  An operation for executing queries in a database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cklocationsortdescriptor)*