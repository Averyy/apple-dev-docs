# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Performs a one-hot encoding on a single input.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func applied(to input: Category?, eventHandler: EventHandler? = nil) throws -> [Int]
```

## Return Value

A one-hot encoded array.

## Discussion

- Parameters

  - input: A category to encode.
  - eventHandler: An event handler.

## See Also

### Performing the transformation
- [func applied<S>(S, eventHandler: EventHandler?) throws -> [[Int]]](./applied%28_,eventhandler%29.md)
  Performs a one-hot encoding on a sequence of inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/onehotencoder/transformer/applied(to:eventhandler:))*