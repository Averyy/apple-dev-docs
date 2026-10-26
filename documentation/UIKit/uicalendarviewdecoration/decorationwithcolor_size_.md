# decorationWithColor:size:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a new calendar view decoration with a filled circle image, using the color and size that you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) decorationWithColor:(UIColor *) color size:(UICalendarViewDecorationSize) size;
```

#### Return Value

A calendar view decoration.

#### Discussion

The color defaults to [`systemFill`](../uicolor/systemfill.md) if you don’t specify it.

The size defaults to .[`UICalendarView.DecorationSize.medium`](../uicalendarview/decorationsize/medium.md) if you don’t specify it.

## Parameters

- `color`: A color for the decoration.
- `size`: A relative size for the decoration.

## See Also

### Creating a Default Decoration View
- [init()](../uicalendarview/decoration/init%28%29.md)
  Creates a default calendar view decoration with a filled circle image, using the system fill color and medium size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarviewdecoration/decorationwithcolor:size:)*