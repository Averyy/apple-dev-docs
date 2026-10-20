# init(inputs:outputs:evaluationFunction:)

**Framework**: Model I/O  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(inputs: [MDLMaterialProperty], outputs: [MDLMaterialProperty], evaluationFunction function: @escaping (MDLMaterialPropertyNode) -> Void)
```

```objc
- (instancetype) initWithInputs:(NSArray<MDLMaterialProperty *> *) inputs outputs:(NSArray<MDLMaterialProperty *> *) outputs evaluationFunction:(void (^)(MDLMaterialPropertyNode *)) function;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialpropertynode/init(inputs:outputs:evaluationfunction:))*