# appIntentsDataSource

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

For more information, refer to [Providing contextual cues to Apple Intelligence and Siri](../../AppIntents/providing-contextual-cues-to-apple-intelligence-and-siri.md) and [App Intents](../../AppIntents/AppIntents.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/appintentsdatasource)*