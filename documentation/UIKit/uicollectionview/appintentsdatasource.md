# appIntentsDataSource

**Framework**: UIKit  
**Kind**: property

The object acting as the collection view’s data source for app entity identifiers that make a cell’s content avdiscoverable by Apple Intelligence and Siri.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@preconcurrency weak var appIntentsDataSource: (any UICollectionViewAppIntentsDataSource)? { get set }
```

#### Discussion

For more information, refer to doc:providing-contextual-cues-to-Apple-Intelligence-and-Siri and [`App Intents`](https://developer.apple.com/documentation/appintents).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/appintentsdatasource)*