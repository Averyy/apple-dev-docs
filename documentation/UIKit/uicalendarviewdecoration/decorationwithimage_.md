# decorationWithImage:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a new calendar view decoration with the image you specify, using the system fill color and medium relative size.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) decorationWithImage:(UIImage *) image;
```

#### Return Value

A calendar view decoration.

#### Discussion

The color defaults to [`systemFill`](../uicolor/systemfill.md) if you don’t specify it.

The size defaults to [`UICalendarView.DecorationSize.medium`](../uicalendarview/decorationsize/medium.md) if you don’t specify it.

## Parameters

- `image`: An image to display as the decoration.

## See Also

### Creating Image Decoration Views
- [- initWithImage:color:size:](./initwithimage_color_size_.md)
  Creates a new calendar view decoration with the image, color, and size that you specify.
- [+ decorationWithImage:color:size:](./decorationwithimage_color_size_.md)
  Creates a new calendar view decoration with the image, color, and size that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarviewdecoration/decorationwithimage:)*