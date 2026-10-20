# functionNames(completionHandler:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

The list of function names in the model asset.

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
func functionNames(completionHandler handler: @escaping @Sendable ([String]?, (any Error)?) -> Void)
```

```swift
var functionNames: [String] { get async throws }
```

```objc
- (void) functionNamesWithCompletionHandler:(void (^)(NSArray<NSString *> *functionNames, NSError *error)) handler;
```

#### Discussion

Some model types (e.g. ML Program) supports multiple functions. Use this method to query the function names.

The method vends the empty array when the model doesn’t use the multi-function configuration.

```swift
let modelAsset = try MLModelAsset(url: modelURL)
let functionNames = try await modelAsset.functionNames
print(functionNames) // For example, ["my_function1", "my_function2"];
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelasset/functionnames(completionhandler:))*