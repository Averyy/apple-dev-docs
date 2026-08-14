# appIntentsDataSource

**Framework**: AppKit  
**Kind**: property

The object acting as the collection view’s data source for app entity identifiers that make a cell’s content discoverable by Apple Intelligence and Siri.

**Availability**:
- macOS 15.4+

## Declaration

```swift
@MainActor
@preconcurrency weak var appIntentsDataSource: (any NSCollectionViewAppIntentsDataSource)? { get set }
```

#### Discussion

For more information, refer to doc:providing-contextual-cues-to-Apple-Intelligence-and-Siri and [`App Intents`](https://developer.apple.com/documentation/appintents).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/appintentsdatasource)*