# endAccessing(identifier:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Type Method

Terminates access to a model collection.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- visionOS 1.0+ - Deprecated in 1.1

> **Deprecated**: Use [Background Assets](../../BackgroundAssets/BackgroundAssets.md) or [`URLSession`](../../Foundation/urlsession.md) instead.

## Declaration

```swift
class func endAccessing(identifier: String) async throws -> Bool
```

```objc
+ (void) endAccessingModelCollectionWithIdentifier:(NSString *) identifier completionHandler:(void (^)(BOOL success, NSError *error)) completionHandler;
```

## Discussion

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

## See Also

### Accessing a model collection
- [+ beginAccessingModelCollectionWithIdentifier:completionHandler:](./beginaccessingmodelcollectionwithidentifier_completionhandler_.md)
  Requests access to a model collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelcollection/endaccessing(identifier:))*