# endDate

**Framework**: Core Data  
**Kind**: property

The end date of the operation that the event represents.

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
var endDate: Date? { get }
```

## See Also

- [var type: NSPersistentCloudKitContainer.EventType](nspersistentcloudkitcontainer/event/type.md)
  The type of event, either setup, import, or export.
- [var identifier: UUID](nspersistentcloudkitcontainer/event/identifier.md)
  A unique identifier for the event in a container.
- [var storeIdentifier: String](nspersistentcloudkitcontainer/event/storeidentifier.md)
  The associated store identifier in the container for the event.
- [var succeeded: Bool](nspersistentcloudkitcontainer/event/succeeded.md)
  A Boolean value that indicates whether the operation the event represents is successful.
- [var startDate: Date](nspersistentcloudkitcontainer/event/startdate.md)
  The start date of the operation that the event represents.
- [var error: (any Error)?](nspersistentcloudkitcontainer/event/error.md)
  An error that indicates why an operation fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/event/enddate)*