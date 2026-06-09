# summary(of:)

**Framework**: Foundation  
**Kind**: method

Returns a summary for the specified unsigned integer array property across the progress subtree.

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
final func summary<P>(of property: KeyPath<ProgressManager.Properties, P.Type>) -> [UInt64] where P : ProgressManager.Property, P.Summary == [UInt64], P.Value == UInt64
```

#### Return Value

The aggregated summary value for the specified property across the entire subtree.

#### Discussion

This method aggregates the values of a custom unsigned integer property from the underlying progress manager and all its children, returning a consolidated summary value as an array.

## Parameters

- `property`: The type of the unsigned integer property to summarize. Must be a property where the value type is `UInt64` and the summary type is `[UInt64]`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressreporter/summary(of:)-2qbq7)*