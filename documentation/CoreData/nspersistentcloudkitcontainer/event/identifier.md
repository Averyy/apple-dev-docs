# identifier

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A unique identifier for the event in a container.

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
var identifier: UUID { get }
```

```objc
@property (nonatomic, strong, readonly) NSUUID * identifier;
```

## See Also

### Inspecting Event Properties
- [var type: NSPersistentCloudKitContainer.EventType](./type.md)
  The type of event, either setup, import, or export.
- [var storeIdentifier: String](./storeidentifier.md)
  The associated store identifier in the container for the event.
- [var succeeded: Bool](./succeeded.md)
  A Boolean value that indicates whether the operation the event represents is successful.
- [var startDate: Date](./startdate.md)
  The start date of the operation that the event represents.
- [var endDate: Date?](./enddate.md)
  The end date of the operation that the event represents.
- [var error: (any Error)?](./error.md)
  An error that indicates why an operation fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/event/identifier)*