# modelContainer

**Framework**: SwiftData  
**Kind**: property

The model container whose data stores this observer monitors for changes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
final let modelContainer: ModelContainer
```

## See Also

- [var eventCounter: Int](historyobserver/eventcounter.md)
  A counter that increments each time the observer detects relevant changes.
- [let observedModels: [any PersistentModel.Type]](historyobserver/observedmodels.md)
  The model types that the observer filters for when evaluating history transactions.
- [let authors: Set<String>](historyobserver/authors.md)
  The transaction authors that the observer filters for when evaluating history transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historyobserver/modelcontainer)*