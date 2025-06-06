# init(objectID:)

**Framework**: Core Data  
**Kind**: init

Returns a cache node for the given managed object ID.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(objectID moid: NSManagedObjectID)
```

#### Return Value

A cache node for the given managed object ID, or `nil` if the node could not be initialized.

## Parameters

- `moid`: A managed object ID.

## See Also

- [Core Data Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstorecachenode/init(objectid:))*