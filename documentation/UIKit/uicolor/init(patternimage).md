# init(patternImage:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a color object using the specified image object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(patternImage image: UIImage)
```

```objc
- (UIColor *) initWithPatternImage:(UIImage *) image;
```

#### Return Value

The pattern color.

#### Discussion

You can use pattern colors to set the fill or stroke color just as you’d a solid color. During drawing, the image in the pattern color is tiled as necessary to cover the given area.

By default, the phase of the returned color is 0, which causes the top-left corner of the image to be aligned with the drawing origin. To change the phase, make the color the current color and then use the [`setPatternPhase(_:)`](../../CoreGraphics/cgcontext/setpatternphase%28_%29.md) function to change the phase.

## Parameters

- `image`: The image to use when creating the pattern color.

## See Also

### Related Documentation
- [+ colorWithPatternImage:](./colorwithpatternimage_.md)
  Creates a color object using the specified image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/init(patternimage:))*