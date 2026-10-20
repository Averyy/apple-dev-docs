# modelDescription(ofFunctionNamed:completionHandler:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

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
func modelDescription(ofFunctionNamed functionName: String, completionHandler handler: @escaping @Sendable (MLModelDescription?, (any Error)?) -> Void)
```

```swift
func modelDescription(of functionName: String) async throws -> MLModelDescription
```

```objc
- (void) modelDescriptionOfFunctionNamed:(NSString *) functionName completionHandler:(void (^)(MLModelDescription *modelDescription, NSError *error)) handler;
```

#### Discussion

Use this method to get the description of the model such as the feature descriptions, the model author, and other metadata.

```swift
let modelAsset = try MLModelAsset(url: modelURL)
let modelDescription = try await modelAsset.modelDescription(of: "my_function")
print(modelDescription)
```

## See Also

### Getting the model description
- [func modelDescription(completionHandler: (MLModelDescription?, (any Error)?) -> Void)](./modeldescription%28completionhandler%29.md)
  The default model descripton.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelasset/modeldescription(offunctionnamed:completionhandler:))*