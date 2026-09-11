# bounds

**Framework**: Media Intelligence  
**Kind**: property

A normalized rectangle describing the location of the face within its source image.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
let bounds: CGRect
```

## Mentions

- [Detecting and grouping faces in images](detecting-and-grouping-faces-in-images.md)

#### Discussion

The rectangle uses normalized coordinates, where `0.0` is the top-left corner and `1.0` is the bottom-right corner along each axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/face/bounds)*