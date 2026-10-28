# modelDescription(completionHandler:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

The default model descripton.

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
func modelDescription(completionHandler handler: @escaping @Sendable (MLModelDescription?, (any Error)?) -> Void)
```

```swift
var modelDescription: MLModelDescription { get async throws }
```

```objc
- (void) modelDescriptionWithCompletionHandler:(void (^)(MLModelDescription *modelDescription, NSError *error)) handler;
```

## Discussion

Use this method to get the description of the model such as the feature descriptions, the model author, and other metadata.

For the multi-function model asset, this method vends the description for the default function. Use `modelDescription(for:)` to get the model description of other functions.

```swift
let modelAsset = try MLModelAsset(url: modelURL)
let modelDescription = try await modelAsset.modelDescription()
print(modelDescription)
```

## See Also

### Getting the model description
- [func modelDescription(ofFunctionNamed: String, completionHandler: (MLModelDescription?, (any Error)?) -> Void)](./modeldescription%28offunctionnamed,completionhandler%29.md)
  The model descripton for a specified function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelasset/modeldescription(completionhandler:))*