# makeContainer(context:)

**Framework**: Swift  
**Kind**: method

Creates a container that represents this array of intent values.

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

An intent value container representing this array.

#### Discussion

This method converts each element in the array to its container representation and wraps them in an `ArrayContainerElement`.

## Parameters

- `context`: The context to use for the conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/makecontainer(context:))*