# classLabels

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

An array of labels, which can be either strings or a numbers, for classifier models.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var classLabels: [Any]? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<id> * classLabels;
```

## See Also

### Accessing metadata
- [var metadata: [MLModelMetadataKey : Any]](./metadata.md)
  A dictionary of the model’s creation information, such as its description, author, version, and license.
- [struct MLModelMetadataKey](../mlmodelmetadatakey.md)
  The set of keys the model uses to store values in its metadata dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodeldescription/classlabels)*