# TranslationSession.Strategy

**Framework**: Translation  
**Kind**: struct

The preferred model to handle translations in your app.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.0+
- macOS 26.4+

## Declaration

```swift
struct Strategy
```

#### Overview

This determines which model your app uses for translating content. The framework uses this strategy when available, or automatically selects an appropriate alternative based on device capabilities and language availability.

## Topics

### Choosing a translation strategy
- [static let highFidelity: TranslationSession.Strategy](translationsession/strategy/highfidelity.md)
  A translation strategy that provides more fluent translations using Apple Intelligence.
- [static let lowLatency: TranslationSession.Strategy](translationsession/strategy/lowlatency.md)
  A translation strategy that provides fast translations using traditional models.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/strategy)*