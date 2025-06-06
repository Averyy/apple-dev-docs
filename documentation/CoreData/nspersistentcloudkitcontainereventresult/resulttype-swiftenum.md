# NSPersistentCloudKitContainerEventResult.ResultType

**Framework**: Core Data  
**Kind**: enum

The types of results from a persistent CloudKit container event fetch request.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
enum ResultType
```

## Topics

### Result Types
- [NSPersistentCloudKitContainerEventResult.ResultType.events](nspersistentcloudkitcontainereventresult/resulttype-swift.enum/events.md)
  The persistent CloudKit container events that match the event request.
- [NSPersistentCloudKitContainerEventResult.ResultType.countEvents](nspersistentcloudkitcontainereventresult/resulttype-swift.enum/countevents.md)
  The number of CloudKit container events that match the event request.
### Initializers
- [init?(rawValue: Int)](nspersistentcloudkitcontainereventresult/resulttype-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var result: Any?](nspersistentcloudkitcontainereventresult/result.md)
  The result of the persistent CloudKit container event request, which the result type determines.
- [var resultType: NSPersistentCloudKitContainerEventResult.ResultType](nspersistentcloudkitcontainereventresult/resulttype-swift.property.md)
  The type of result that the CloudKit container event fetch request returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainereventresult/resulttype-swift.enum)*