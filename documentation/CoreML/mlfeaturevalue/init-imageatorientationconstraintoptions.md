# init(imageAt:orientation:constraint:options:)

**Framework**: Core ML  
**Kind**: init

Construct image feature value from an image on disk using a model specified image constraint. The passed in orientation supersedes any in the file

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
convenience init(imageAt url: URL, orientation: CGImagePropertyOrientation, constraint: MLImageConstraint, options: [MLFeatureValue.ImageOption : Any]? = nil) throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeaturevalue/init(imageat:orientation:constraint:options:))*