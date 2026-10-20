# modelDescription(ofFunctionNamed:completionHandler:)

**Framework**: Core ML  
**Kind**: method

The model descripton for a specified function.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func modelDescription(of functionName: String) async throws -> MLModelDescription
```

#### Discussion

Use this method to get the description of the model such as the feature descriptions, the model author, and other metadata.

```swift
let modelAsset = try MLModelAsset(url: modelURL)
let modelDescription = try await modelAsset.modelDescription(of: "my_function")
print(modelDescription)
```

## See Also

- [func modelDescription(completionHandler: (MLModelDescription?, (any Error)?) -> Void)](mlmodelasset/modeldescription(completionhandler:).md)
  The default model descripton.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelasset/modeldescription(offunctionnamed:completionhandler:))*