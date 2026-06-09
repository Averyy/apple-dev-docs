# merge(_:_:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Merges two summary values into a single combined summary.

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
static func merge(_ summary1: Self.Summary, _ summary2: Self.Summary) -> Self.Summary
```

#### Return Value

A new summary that represents the combination of both input summaries.

#### Discussion

This method is called to combine summary values from different branches of the progress manager hierarchy into a unified summary.

## Parameters

- `summary1`: The first summary to merge.
- `summary2`: The second summary to merge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressmanager/property/merge(_:_:))*