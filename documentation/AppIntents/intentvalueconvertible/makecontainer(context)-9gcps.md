# makeContainer(context:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Instance Method

Creates an intent value container that represents this wrapper.

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

An intent value container representing this wrapper.

#### Discussion

This implementation delegates to the base value’s container creation method, ensuring that the wrapper behaves consistently with its underlying type.

## Parameters

- `context`: The context to use for the conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentvalueconvertible/makecontainer(context:)-9gcps)*