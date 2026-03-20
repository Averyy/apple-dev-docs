# random(using:)

**Framework**: Foundation  
**Kind**: method

Generates a new random UUID.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

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