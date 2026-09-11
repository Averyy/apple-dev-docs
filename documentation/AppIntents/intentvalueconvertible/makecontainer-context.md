# makeContainer(context:)

**Framework**: App Intents  
**Kind**: method  
**Required**: Yes

Creates an intent value container that represents this value.

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

An intent value container representing this value.

#### Discussion

This method converts the value to a type-erased container that App Intents can use. The container encapsulates the value and provides mechanisms for type-safe access and conversion.

## Parameters

- `context`: The context to use for the conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentvalueconvertible/makecontainer(context:))*