# filter(runBoundaries:)

**Framework**: Foundation  
**Kind**: method

Returns a copy of the attribute container with only attributes that have the provided run boundaries.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

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