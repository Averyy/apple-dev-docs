# filter(inheritedByAddedText:)

**Framework**: Foundation  
**Kind**: method

Returns a copy of the attribute container with only attributes that specify the provided inheritance behavior.

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
func filter(inheritedByAddedText: Bool) -> AttributeContainer
```

#### Return Value

A copy of the attribute container with only attributes whose `inheritedByAddedText` property matches the provided value.

## Parameters

- `inheritedByAddedText`: An   value to filter. Attributes matching this value are included in the returned container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributecontainer/filter(inheritedbyaddedtext:))*