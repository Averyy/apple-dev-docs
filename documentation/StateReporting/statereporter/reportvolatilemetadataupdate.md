# reportVolatileMetadataUpdate(_:)

**Framework**: StateReporting  
**Kind**: method

Updates the volatile metadata within the current state without beginning a new transition.

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
final func reportVolatileMetadataUpdate(_ updatedMetadata: VolatileMetadata?)
```

## Mentions

- [Getting started with StateReporting](getting-started-with-statereporting.md)

#### Discussion

Use this method to update rapidly-changing data — such as a progress value or a running count — while staying within the same state. If no state is currently active, this call is a no-op. Calling this method more frequently than user interaction timescales can trigger rate limiting, causing updates to go unlogged.

## Parameters

- `updatedMetadata`: The updated volatile metadata, or `nil` to clear volatile context without ending the current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/statereporting/statereporter/reportvolatilemetadataupdate(_:))*