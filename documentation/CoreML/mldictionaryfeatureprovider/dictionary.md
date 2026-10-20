# dictionary

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

The backing dictionary.

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
var dictionary: [String : MLFeatureValue] { get }
```

```objc
@property (nonatomic, readonly) NSDictionary<NSString *,MLFeatureValue *> * dictionary;
```

## See Also

### Accessing the features
- [subscript(String) -> MLFeatureValue?](./subscript%28_%29.md)
  Subscript interface for the feature provider to pass through to the dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mldictionaryfeatureprovider/dictionary)*