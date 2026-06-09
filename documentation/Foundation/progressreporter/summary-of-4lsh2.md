# summary(of:)

**Framework**: Foundation  
**Kind**: method

Returns a summary for the specified double property across the progress subtree.

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
final func summary<P>(of property: KeyPath<ProgressManager.Properties, P.Type>) -> Double where P : ProgressManager.Property, P.Summary == Double, P.Value == Double
```

#### Return Value

The aggregated summary value for the specified property across the entire subtree.

#### Discussion

This method aggregates the values of a custom double property from the underlying progress manager and all its children, returning a consolidated summary value.

## Parameters

- `property`: The type of the double property to summarize. Must be a property where both the value and summary types are `Double`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressreporter/summary(of:)-4lsh2)*