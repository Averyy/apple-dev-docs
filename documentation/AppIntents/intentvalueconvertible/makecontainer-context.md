# makeContainer(context:)

**Framework**: App Intents  
**Kind**: method  
**Required**: Yes

Creates an intent value container that represents this value.

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