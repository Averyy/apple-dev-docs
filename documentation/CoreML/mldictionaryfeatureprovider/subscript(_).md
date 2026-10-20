# subscript(_:)

**Framework**: Core ML  
**Kind**: subscript  
**Role**: Instance Subscript

Subscript interface for the feature provider to pass through to the dictionary.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
subscript(featureName: String) -> MLFeatureValue? { get }
```

```objc
- (MLFeatureValue *) objectForKeyedSubscript:(NSString *) featureName;
```

## See Also

### Accessing the features
- [var dictionary: [String : MLFeatureValue]](./dictionary.md)
  The backing dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mldictionaryfeatureprovider/subscript(_:))*