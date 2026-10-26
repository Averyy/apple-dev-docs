# initWithImage:color:size:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Creates a new calendar view decoration with the image, color, and size that you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
- (instancetype) initWithImage:(UIImage *) image color:(UIColor *) color size:(UICalendarViewDecorationSize) size;
```

#### Return Value

A calendar view decoration.

#### Discussion

The image defaults to `circlebadge.fill` if you don’t specify it.

The color defaults to [`systemFill`](../uicolor/systemfill.md) if you don’t specify it.

The size defaults to [`UICalendarView.DecorationSize.medium`](../uicalendarview/decorationsize/medium.md) if you don’t specify it.

## Parameters

- `image`: An image to display as the decoration.
- `color`: A color for the decoration.
- `size`: A relative size for the decoration.

## See Also

### Creating Image Decoration Views
- [+ decorationWithImage:](./decorationwithimage_.md)
  Creates a new calendar view decoration with the image you specify, using the system fill color and medium relative size.
- [+ decorationWithImage:color:size:](./decorationwithimage_color_size_.md)
  Creates a new calendar view decoration with the image, color, and size that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarviewdecoration/initwithimage:color:size:)*