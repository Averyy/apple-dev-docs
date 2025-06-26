# init(key:relativeLocation:)

**Framework**: CloudKit  
**Kind**: init

Creates a location sort descriptor using the specified key and relative location.

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
init(key: String, relativeLocation: CLLocation)
```

#### Discussion

During sorting, the sort descriptor computes the distance between the value in the `relativeLocation` parameter and the location value in the specified key of each record. It then sorts the records in ascending order using the distance between the two points. You can’t change the sort order.

## Parameters

- `key`: The name of the key with a   object as its value. The key must belong to the records you’re sorting. The sort descriptor uses this key to retrieve the corresponding value from the record.
- `relativeLocation`: The reference location when sorting. CloudKit sorts records according to their distance from this location.

## See Also

- [init(coder: NSCoder)](cklocationsortdescriptor/init(coder:).md)
  Creates a location sort descriptor from a serialized instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cklocationsortdescriptor/init(key:relativelocation:))*