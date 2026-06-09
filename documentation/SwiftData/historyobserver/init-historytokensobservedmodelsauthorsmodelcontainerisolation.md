# init(historyTokens:observedModels:authors:modelContainer:isolation:)

**Framework**: SwiftData  
**Kind**: init

Creates a history observer that reports changes through its observable [`eventCounter`](historyobserver/eventcounter.md) property.

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
convenience init(historyTokens: [String : any HistoryToken]? = nil, observedModels: [any PersistentModel.Type] = [], authors: Set<String> = [], modelContainer: ModelContainer, isolation: isolated (any Actor)? = #isolation) throws
```

#### Discussion

Use this initializer when you want to observe history changes via SwiftUI’s observation system or by reading [`eventCounter`](historyobserver/eventcounter.md) directly.

> **Note**: An error if the observer fails to fetch the initial history tokens.

## Parameters

- `historyTokens`: The initial history tokens keyed by store identifier. When `nil`, the observer starts with an empty token set and captures tokens from the first notification for each store.
- `observedModels`: The model types to filter for. When empty (the default), the observer responds to changes for any model.
- `authors`: The transaction authors to filter for. When empty (the default), the observer responds to changes from any author.
- `modelContainer`: The model container to observe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historyobserver/init(historytokens:observedmodels:authors:modelcontainer:isolation:))*