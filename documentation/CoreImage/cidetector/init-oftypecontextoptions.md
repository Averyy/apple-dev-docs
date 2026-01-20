# init(ofType:context:options:)

**Framework**: Core Image  
**Kind**: init

Creates and returns a configured detector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
init?(ofType type: String, context: CIContext?, options: [String : Any]? = nil)
```

#### Return Value

A configured detector.

#### Discussion

A [`CIDetector`](cidetector.md) object can potentially create and hold a significant amount of resources. Where possible, reuse the same [`CIDetector`](cidetector.md) instance. Also, when processing images with a detector object, your application performs better if the [`CIContext`](cicontext.md) used to initialize the detector is the same context used to process the [`ciImage`](https://developer.apple.com/documentation/UIKit/UIImage/ciImage) objects.

## Parameters

- `type`: A string indicating the kind of detector you are interested in. See  .
- `context`: A Core Image context that the detector can use when analyzing an image.
- `options`: A dictionary containing details on how you want the detector to be configured. See  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidetector/init(oftype:context:options:))*