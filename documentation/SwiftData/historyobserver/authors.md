# authors

**Framework**: SwiftData  
**Kind**: property

The transaction authors that the observer filters for when evaluating history transactions.

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
final let authors: Set<String>
```

#### Discussion

When non-empty, the observer only reports changes whose transactions were written by one of the specified authors. When empty, the observer treats transactions from any author as relevant.

## See Also

- [var eventCounter: Int](historyobserver/eventcounter.md)
  A counter that increments each time the observer detects relevant changes.
- [let modelContainer: ModelContainer](historyobserver/modelcontainer.md)
  The model container whose data stores this observer monitors for changes.
- [let observedModels: [any PersistentModel.Type]](historyobserver/observedmodels.md)
  The model types that the observer filters for when evaluating history transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historyobserver/authors)*