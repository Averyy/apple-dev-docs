# reportTransition(to:stableMetadata:volatileMetadata:)

**Framework**: StateReporting  
**Kind**: method

Reports a transition to a new state.

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
final func reportTransition(to stateLabel: String?, stableMetadata: StableMetadata? = nil, volatileMetadata: VolatileMetadata? = nil)
```

## Mentions

- [Getting started with StateReporting](getting-started-with-statereporting.md)

#### Discussion

A transition occurs only when `stateLabel` or `stableMetadata` changes from the current state. If both are equal to the current values, this call is a no-op. Pass `nil` for `stateLabel` to indicate that no state is currently active, clearing any previously reported state. Passing an empty string for `stateLabel` is a fatal error. Any volatile metadata from the previous state is discarded when a new transition begins. Calling this method more frequently than user interaction timescales can trigger rate limiting, causing state updates to go unlogged.

## Parameters

- `stateLabel`: A descriptive label for the new state, which must not be empty, or `nil` to clear the active state.
- `stableMetadata`: An optional value that identifies the state together with `stateLabel`.
- `volatileMetadata`: An optional value providing context likely to change within this state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/statereporting/statereporter/reporttransition(to:stablemetadata:volatilemetadata:))*