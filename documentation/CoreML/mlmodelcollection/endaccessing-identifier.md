# endAccessing(identifier:)

**Framework**: Core ML  
**Kind**: method

Terminates access to a model collection.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func endAccessing(identifier: String) async throws -> Bool
```

#### Discussion

Use this method when your app no longer needs access to a model collection.

**Swift**:

```swift
MLModelCollection.endAccessing(identifier: modelCollectionName) { result in
    switch result {
    case .success():
        print("Successfully ended access to `\(modelCollectionName)`.")

    case .failure(let error):
        print("Error ending access to `\(modelCollectionName)`: \(error)")
    }
}
```

**Objective-C**:

```objc
[MLModelCollection endAccessingModelCollectionWithIdentifier:modelCollectionName
                                           completionHandler:^(BOOL success,
                                                               NSError * _Nullable error) {
    if (success) {
        NSLog(@"Successfully ended access to `%@`.", modelCollectionName);
    }
    else {
        NSLog(@"Error ending access to `%@`: %@", modelCollectionName, error);
    }
}];
```

## Parameters

- `identifier`: The name of the model collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelcollection/endaccessing(identifier:))*