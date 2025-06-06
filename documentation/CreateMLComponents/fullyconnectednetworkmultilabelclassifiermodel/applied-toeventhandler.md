# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs a classification on a shaped array.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func applied(to input: MLShapedArray<Scalar>, eventHandler: EventHandler? = nil) throws -> ClassificationDistribution<Label>
```

#### Return Value

A classification distribution.

## Parameters

- `input`: The classifier input.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkmultilabelclassifiermodel/applied(to:eventhandler:))*