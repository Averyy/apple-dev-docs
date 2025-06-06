# init(parameters:)

**Framework**: Core ML  
**Kind**: init  
**Required**: Yes

Initializes the custom layer implementation.

**Availability**:
- iOS 11.2+
- iPadOS 11.2+
- Mac Catalyst 13.1+
- macOS 10.13.2+
- tvOS 11.2+
- visionOS 1.0+
- watchOS 4.2+

## Declaration

```swift
init(parameters: [String : Any]) throws
```

## Mentions

- [Creating and Integrating a Model with Custom Layers](creating-and-integrating-a-model-with-custom-layers.md)

#### Discussion

Implement this method to initialize your custom layer. It is called once, at load time. Use the parameters to configure the custom layer as needed.

If the layer cannot be initialized, your implementation should throw a [`customLayer`](mlmodelerror-swift.struct/customlayer.md) error.

## Parameters

- `parameters`: The contents of the parameter dictionary from the   file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcustomlayer/init(parameters:))*