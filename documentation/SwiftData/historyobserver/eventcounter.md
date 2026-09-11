# eventCounter

**Framework**: SwiftData  
**Kind**: property

A counter that increments each time the observer detects relevant changes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
final var eventCounter: Int { get }
```

#### Discussion

The observer increments this value when it processes a remote change notification that contains transactions matching its criteria. You can observe this property from a SwiftUI view to trigger a UI update.

## See Also

- [let modelContainer: ModelContainer](historyobserver/modelcontainer.md)
  The model container whose data stores this observer monitors for changes.
- [let observedModels: [any PersistentModel.Type]](historyobserver/observedmodels.md)
  The model types that the observer filters for when evaluating history transactions.
- [let authors: Set<String>](historyobserver/authors.md)
  The transaction authors that the observer filters for when evaluating history transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historyobserver/eventcounter)*