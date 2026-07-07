# init(_:description:scale:)

**Framework**: Evaluations  
**Kind**: init

Creates a scoring dimension.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(_ name: String, description: String? = nil, scale: ScoringScale)
```

## Parameters

- `name`: The dimension name, used as the DataFrame column name and for aggregation lookup.
- `description`: Optional description providing context about what this dimension measures.
- `scale`: The scoring scale for this dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/scoredimension/init(_:description:scale:))*