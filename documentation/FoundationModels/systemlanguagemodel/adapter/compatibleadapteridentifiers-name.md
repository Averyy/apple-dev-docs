# compatibleAdapterIdentifiers(name:)

**Framework**: Foundation Models  
**Kind**: method

Get all compatible adapter identifiers compatible with current system models.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static func compatibleAdapterIdentifiers(name: String) -> [String]
```

#### Return Value

All adapter identifiers compatible with current system models, listed in descending order in terms of system preference. You can determine which asset pack or on-demand resource to download with compatible adapter identifiers.

On devices that support Apple Intelligence, the result is guaranteed to be non-empty.

## Parameters

- `name`: Name of the adapter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/adapter/compatibleadapteridentifiers(name:))*