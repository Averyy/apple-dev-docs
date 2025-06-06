# metadata

**Framework**: Core ML  
**Kind**: property

A dictionary of the model’s creation information, such as its description, author, version, and license.

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
var metadata: [MLModelMetadataKey : Any] { get }
```

#### Discussion

Use the keys defined by [`MLModelMetadataKey`](mlmodelmetadatakey.md) to retrieve the dictionary’s entries.

## See Also

- [var classLabels: [Any]?](mlmodeldescription/classlabels.md)
  An array of labels, which can be either strings or a numbers, for classifier models.
- [struct MLModelMetadataKey](mlmodelmetadatakey.md)
  The set of keys the model uses to store values in its metadata dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodeldescription/metadata)*