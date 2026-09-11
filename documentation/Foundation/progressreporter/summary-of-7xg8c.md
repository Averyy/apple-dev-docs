# summary(of:)

**Framework**: Foundation  
**Kind**: method

Returns a summary for the specified unsigned integer property across the progress subtree.

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
final func summary<P>(of property: KeyPath<ProgressManager.Properties, P.Type>) -> UInt64 where P : ProgressManager.Property, P.Summary == UInt64, P.Value == UInt64
```

#### Return Value

The aggregated summary value for the specified property across the entire subtree.

#### Discussion

This method aggregates the values of a custom unsigned integer property from the underlying progress manager and all its children, returning a consolidated summary value.

## Parameters

- `property`: The type of the unsigned property to summarize. Must be a property where both the value and summary types are `UInt64`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressreporter/summary(of:)-7xg8c)*