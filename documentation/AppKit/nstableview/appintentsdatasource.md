# appIntentsDataSource

**Framework**: AppKit  
**Kind**: property

The object acting as the table view’s data source for app entity identifiers that make a cell’s content discoverable by Apple Intelligence and Siri.

**Availability**:
- macOS 15.4+

## Declaration

```swift
@MainActor
@preconcurrency weak var appIntentsDataSource: (any NSTableViewAppIntentsDataSource)? { get set }
```

#### Discussion

For more information, refer to doc:Making-onscreen-content-available-to-siri-and-apple-intelligence and [`App Intents`](https://developer.apple.com/documentation/AppIntents).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/appintentsdatasource)*