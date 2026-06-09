# StateReporter

**Framework**: StateReporting  
**Kind**: class

An object unique per domain that records state transitions and volatile metadata updates.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
final class StateReporter<StableMetadata, VolatileMetadata> where StableMetadata : ReportableMetadata, VolatileMetadata : ReportableMetadata
```

## Mentions

- [Getting started with StateReporting](getting-started-with-statereporting.md)

#### Overview

`StateReporter` is the central object for recording your feature’s or subsystem’s current state. You obtain an instance through the [`reporter(for:stableMetadata:volatileMetadata:)`](statereporter/reporter(for:stablemetadata:volatilemetadata:).md) method, which guarantees that every caller using the same domain string receives the same object. Attempting to call the method with different generic type arguments for an already-registered domain is a fatal error.

A state is uniquely identified by the combination of a label and stable metadata. A transition to a new state occurs when either changes; reporting the same label and stable metadata is a no-op. *Volatile metadata* provides additional context within an ongoing state and is discarded when the next transition begins. Both stable and volatile metadata are expressed as types conforming to [`ReportableMetadata`](reportablemetadata.md), which can be synthesized automatically with the [`ReportableMetadata()`](reportablemetadata().md) macro.

Call [`reportTransition(to:stableMetadata:volatileMetadata:)`](statereporter/reporttransition(to:stablemetadata:volatilemetadata:).md) whenever your feature transitions to a new state. Pass `nil` as the label to signal that no state is active. Call [`reportVolatileMetadataUpdate(_:)`](statereporter/reportvolatilemetadataupdate(_:).md) to update volatile metadata without beginning a new state transition. Calling either method more frequently than user interaction timescales can trigger rate limiting, causing state updates to go unlogged.

```swift
let reporter = StateReporter.reporter(
    for: "com.example.myapp.checkout",
    stableMetadata:AppMetadata.self,
    volatileMetadata:SessionMetadata.self
)

reporter.reportTransition(
    to: "paymentSheet",
    stableMetadata: AppMetadata(userTier: .premium),
    volatileMetadata: SessionMetadata(cartTotal: 49.99)
)
```

For Objective-C, use [`SRStateReporter`](srstatereporter.md).

## Topics

### Instance Properties
- [let domain: String](statereporter/domain.md)
  The reverse DNS-style domain name that identifies this reporter.
### Instance Methods
- [func reportTransition(to: String?, stableMetadata: StableMetadata?, volatileMetadata: VolatileMetadata?)](statereporter/reporttransition(to:stablemetadata:volatilemetadata:).md)
  Reports a transition to a new state.
- [func reportVolatileMetadataUpdate(VolatileMetadata?)](statereporter/reportvolatilemetadataupdate(_:).md)
  Updates the volatile metadata within the current state without beginning a new transition.
### Type Methods
- [static func reporter(for: String, stableMetadata: StableMetadata.Type, volatileMetadata: VolatileMetadata.Type) -> StateReporter<StableMetadata, VolatileMetadata>](statereporter/reporter(for:stablemetadata:volatilemetadata:).md)
  Returns the reporter instance unique to the given domain and metadata types.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/statereporting/statereporter)*