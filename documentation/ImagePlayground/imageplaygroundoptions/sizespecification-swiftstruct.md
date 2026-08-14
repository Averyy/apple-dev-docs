# ImagePlaygroundOptions.SizeSpecification

**Framework**: Image Playground  
**Kind**: struct

A type that specifies image size and aspect ratio information.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SizeSpecification
```

#### Overview

The Image Playground framework supports the creation of images with a finite set of sizes and aspect ratios. To request an image of a particular size, call the static [`closest(to:)`](imageplaygroundoptions/sizespecification-swift.struct/closest(to:).md) method to create an instance of this structure. That method creates a structure with a supported size that most closely matches the size information you provided. The method considers both the resolution and aspect ratio you specified.

Assign an instance of this structure to the [`sizeSpecification`](imageplaygroundoptions/sizespecification-swift.property.md) property of your options, and use those options to generate your image.

## Topics

### Type Methods
- [static func closest(to: CGSize) -> ImagePlaygroundOptions.SizeSpecification](imageplaygroundoptions/sizespecification-swift.struct/closest(to:).md)
  Creates a new instance of this structure with a size value that best matches the specified size.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundoptions/sizespecification-swift.struct)*