# startDate

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The start date of the operation that the event represents.

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
var startDate: Date { get }
```

```objc
@property (nonatomic, strong, readonly) NSDate * startDate;
```

## See Also

### Inspecting Event Properties
- [var type: NSPersistentCloudKitContainer.EventType](./type.md)
  The type of event, either setup, import, or export.
- [var identifier: UUID](./identifier.md)
  A unique identifier for the event in a container.
- [var storeIdentifier: String](./storeidentifier.md)
  The associated store identifier in the container for the event.
- [var succeeded: Bool](./succeeded.md)
  A Boolean value that indicates whether the operation the event represents is successful.
- [var endDate: Date?](./enddate.md)
  The end date of the operation that the event represents.
- [var error: (any Error)?](./error.md)
  An error that indicates why an operation fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/event/startdate)*