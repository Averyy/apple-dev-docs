# summary(of:)

**Framework**: Foundation  
**Kind**: method

Returns a summary for a custom URL property across the progress subtree.

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
final func summary<P>(of property: KeyPath<ProgressManager.Properties, P.Type>) -> P.Summary where P : ProgressManager.Property, P.Summary == [URL?], P.Value == URL?
```

#### Return Value

A `[URL?]` summary value for the specified property.

#### Discussion

This method aggregates the values of a custom URL property from this progress manager and all its children, returning a consolidated summary value as an array of URLs.

## Parameters

- `property`: The type of the URL property to summarize. Must be a property where the value type is `URL?` and the summary type is `[URL?]`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressmanager/summary(of:)-3kyy8)*