# makeContainer(context:)

**Framework**: Foundation  
**Kind**: method

Creates a container that represents the attributed string.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func makeContainer(context: IntentValueContainer.ConversionContext) -> IntentValueContainer
```

#### Return Value

An intent value container representing this attributed string.

#### Discussion

This method converts the `AttributedString` to an `NSAttributedString` and wraps it in an intent value container.

## Parameters

- `context`: The context to use for the conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/makecontainer(context:))*