# reporter(for:stableMetadata:volatileMetadata:)

**Framework**: StateReporting  
**Kind**: method

Returns the reporter instance unique to the given domain and metadata types.

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
static func reporter(for domain: String, stableMetadata stableMetadataType: StableMetadata.Type = Never.self, volatileMetadata volatileMetadataType: VolatileMetadata.Type = Never.self) -> StateReporter<StableMetadata, VolatileMetadata>
```

## Mentions

- [Getting started with StateReporting](getting-started-with-statereporting.md)

#### Return Value

The reporter instance for the specified domain.

#### Discussion

This method is the only way to obtain a `StateReporter`. Calling it multiple times with the same domain string always returns the same object. Calling it with a domain string that was previously registered under different generic type arguments is a fatal error.

## Parameters

- `domain`: The reverse DNS-style domain name.
- `stableMetadataType`: The type to use for stable metadata (defaults to `Never`).
- `volatileMetadataType`: The type to use for volatile metadata (defaults to `Never`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/statereporting/statereporter/reporter(for:stablemetadata:volatilemetadata:))*