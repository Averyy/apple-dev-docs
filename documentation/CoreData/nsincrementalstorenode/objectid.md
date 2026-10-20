# objectID

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The object ID that identifies the data stored by the receiver.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var objectID: NSManagedObjectID { get }
```

```objc
@property (nonatomic, strong, readonly) NSManagedObjectID * objectID;
```

## See Also

### Managing Node Data
- [func update(withValues: [String : Any], version: UInt64)](./update%28withvalues,version%29.md)
  Update the values and version to reflect new data being saved to or loaded from the external store.
- [func value(for: NSPropertyDescription) -> Any?](./value%28for%29.md)
  Returns the value for the given property.
- [var version: UInt64](./version.md)
  The version of data in the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/objectid)*