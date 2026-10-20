# init(array:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates the batch provider based on the array of feature providers.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
init(array: [any MLFeatureProvider])
```

```objc
- (instancetype) initWithFeatureProviderArray:(NSArray<id<MLFeatureProvider>> *) array;
```

## Parameters

- `array`: The array of feature providers for the batch.

## See Also

### Creating a batch provider
- [init(dictionary: [String : [Any]]) throws](./init%28dictionary%29.md)
  Creates a batch provider based on feature names and their associated arrays of data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlarraybatchprovider/init(array:))*