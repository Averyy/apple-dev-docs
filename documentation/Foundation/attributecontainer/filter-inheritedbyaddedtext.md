# filter(inheritedByAddedText:)

**Framework**: Foundation  
**Kind**: method

Returns a copy of the attribute container with only attributes that specify the provided inheritance behavior.

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
func filter(inheritedByAddedText: Bool) -> AttributeContainer
```

#### Return Value

A copy of the attribute container with only attributes whose `inheritedByAddedText` property matches the provided value.

## Parameters

- `inheritedByAddedText`: An   value to filter. Attributes matching this value are included in the returned container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributecontainer/filter(inheritedbyaddedtext:))*