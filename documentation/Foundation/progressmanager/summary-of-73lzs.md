# summary(of:)

**Framework**: Foundation  
**Kind**: method

Returns a summary for a custom duration property across the progress subtree.

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
final func summary<P>(of property: KeyPath<ProgressManager.Properties, P.Type>) -> P.Summary where P : ProgressManager.Property, P.Summary == Duration, P.Value == Duration
```

#### Return Value

A `Duration` summary value for the specified property.

#### Discussion

This method aggregates the values of a custom duration property from this progress manager and all its children, returning a consolidated summary value.

## Parameters

- `property`: The type of the duration property to summarize. Must be a property where the value type is `Duration` and the summary type is `Duration`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressmanager/summary(of:)-73lzs)*