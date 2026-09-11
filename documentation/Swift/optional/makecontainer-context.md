# makeContainer(context:)

**Framework**: Swift  
**Kind**: method

Creates a container that represents this optional intent value.

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

An intent value container representing this optional value.

#### Discussion

If the optional is `nil`, it creates a container that resolves to a null vlaue. If the optional isn’t `nil`, it delegates the conversation to the wrapped value’s container creation.

## Parameters

- `context`: The context to use for the conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/makecontainer(context:))*