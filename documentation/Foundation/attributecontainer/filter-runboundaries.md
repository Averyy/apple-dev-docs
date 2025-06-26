# filter(runBoundaries:)

**Framework**: Foundation  
**Kind**: method

Returns a copy of the attribute container with only attributes that have the provided run boundaries.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func filter(runBoundaries: AttributedString.AttributeRunBoundaries?) -> AttributeContainer
```

#### Return Value

A copy of the attribute container with only attributes whose `runBoundaries` property matches the provided value.

## Parameters

- `runBoundaries`: The required   value of the filtered attributes. If   is provided, only attributes not bound to any specific boundary will be returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributecontainer/filter(runboundaries:))*