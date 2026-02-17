# random(using:)

**Framework**: Foundation  
**Kind**: method

Generates a new random UUID.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- tvOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)
- watchOS 26.4+ (Beta)

## Declaration

```swift
static func random(using generator: inout some RandomNumberGenerator) -> UUID
```

#### Return Value

A random UUID.

## Parameters

- `generator`: The random number generator to use when creating the new random value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/uuid/random(using:))*