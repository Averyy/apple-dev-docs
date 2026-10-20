# NSPersistentCloudKitContainerEventResult.ResultType

**Framework**: Core Data  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NSPersistentCloudKitContainerEventResultType : NSInteger;
```

## Topics

### Result Types
- [NSPersistentCloudKitContainerEventResult.ResultType.events](./resulttype-swift.enum/events.md)
  The persistent CloudKit container events that match the event request.
- [NSPersistentCloudKitContainerEventResult.ResultType.countEvents](./resulttype-swift.enum/countevents.md)
  The number of CloudKit container events that match the event request.
### Initializers
- [init?(rawValue: Int)](./resulttype-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling Event Results
- [var result: Any?](./result.md)
  The result of the persistent CloudKit container event request, which the result type determines.
- [var resultType: NSPersistentCloudKitContainerEventResult.ResultType](./resulttype-swift.property.md)
  The type of result that the CloudKit container event fetch request returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainereventresult/resulttype-swift.enum)*