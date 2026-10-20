# DataStoreBatchDeleteRequest

**Framework**: SwiftData  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+
- Swift 5.9+

## Declaration

```swift
struct DataStoreBatchDeleteRequest<T> where T : PersistentModel
```

## Topics

### Instance Properties
- [let editingState: EditingState](./datastorebatchdeleterequest/editingstate.md)
- [let includeSubclasses: Bool](./datastorebatchdeleterequest/includesubclasses.md)
- [let predicate: Predicate<T>?](./datastorebatchdeleterequest/predicate.md)

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Deleting persisted model data
- [func delete<T>(DataStoreBatchDeleteRequest<T>) throws](./datastorebatching/delete%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/datastorebatchdeleterequest)*