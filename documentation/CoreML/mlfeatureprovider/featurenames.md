# featureNames

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The set of valid feature names.

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
var featureNames: Set<String> { get }
```

```objc
@property (nonatomic, readonly) NSSet<NSString *> * featureNames;
```

## See Also

### Accessing values
- [func featureValue(for: String) -> MLFeatureValue?](./featurevalue%28for%29.md)
  Accesses the feature value given the feature’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeatureprovider/featurenames)*