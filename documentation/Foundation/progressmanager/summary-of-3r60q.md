# summary(of:)

**Framework**: Foundation  
**Kind**: method

Returns a summary for a custom integer property across the progress subtree.

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
final func summary<P>(of property: KeyPath<ProgressManager.Properties, P.Type>) -> P.Summary where P : ProgressManager.Property, P.Summary == Int, P.Value == Int
```

#### Return Value

An `Int` summary value for the specified property.

#### Discussion

This method aggregates the values of a custom integer property from this progress manager and all its children, returning a consolidated summary value.

## Parameters

- `property`: The type of the integer property to summarize. Must be a property where both the value and summary types are `Int`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressmanager/summary(of:)-3r60q)*