# modelContext

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The SwiftData model context that will be used for queries and other model operations within this environment.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
var modelContext: ModelContext { get set }
```

## See Also

### Global objects
- [var calendar: Calendar](./calendar.md)
  The current calendar that views should use when handling dates.
- [var documentConfiguration: DocumentConfiguration?](./documentconfiguration.md)
  The configuration of a document in a [`DocumentGroup`](../documentgroup.md).
- [var locale: Locale](./locale.md)
  The current locale that views should use.
- [var managedObjectContext: NSManagedObjectContext](./managedobjectcontext.md)
- [var timeZone: TimeZone](./timezone.md)
  The current time zone that views should use when handling dates.
- [var undoManager: UndoManager?](./undomanager.md)
  The undo manager used to register a view’s undo operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/modelcontext)*