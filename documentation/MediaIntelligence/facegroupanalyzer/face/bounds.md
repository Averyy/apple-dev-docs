# bounds

**Framework**: Media Intelligence  
**Kind**: property

A normalized rectangle describing the location of the face within its source image.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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