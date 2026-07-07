# modelContext

**Framework**: SwiftUI  
**Kind**: property

The SwiftData model context that will be used for queries and other model operations within this environment.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
var modelContext: ModelContext { get set }
```

## See Also

- [var calendar: Calendar](environmentvalues/calendar.md)
  The current calendar that views should use when handling dates.
- [var documentConfiguration: DocumentConfiguration?](environmentvalues/documentconfiguration.md)
  The configuration of a document in a [`DocumentGroup`](documentgroup.md).
- [var locale: Locale](environmentvalues/locale.md)
  The current locale that views should use.
- [var managedObjectContext: NSManagedObjectContext](environmentvalues/managedobjectcontext.md)
- [var timeZone: TimeZone](environmentvalues/timezone.md)
  The current time zone that views should use when handling dates.
- [var undoManager: UndoManager?](environmentvalues/undomanager.md)
  The undo manager used to register a view’s undo operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/modelcontext)*