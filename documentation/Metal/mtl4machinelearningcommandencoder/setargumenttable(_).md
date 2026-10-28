# setArgumentTable(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets an argument table for the command encoder’s machine learning shader stage.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setArgumentTable(_ argumentTable: (any MTL4ArgumentTable)?)
```

```objc
- (void) setArgumentTable:(id<MTL4ArgumentTable>) argumentTable;
```

## Discussion

The argument table provides inputs to all subsequent Machine Learning dispatches.

## Parameters

- `argumentTable`: An argument table to set on the command encoder’s Machine Learning stage.

## See Also

### Configuring the pass
- [func setPipelineState(any MTL4MachineLearningPipelineState)](./setpipelinestate%28_%29.md)
  Configures the encoder with a machine learning pipeline state instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4machinelearningcommandencoder/setargumenttable(_:))*