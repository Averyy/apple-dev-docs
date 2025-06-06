# init(text:detailText:image:showsDisclosureIndicator:)

**Framework**: CarPlay  
**Kind**: init

Creates a list item with primary text, secondary text, an image, and a disclosure indicator.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(text: String?, detailText: String?, image: UIImage?, showsDisclosureIndicator: Bool)
```

#### Return Value

A newly initialized list item.

## Parameters

- `text`: The primary text to show in the list item cell.
- `detailText`: Additional text to display below the primary text in the list item cell.
- `image`: The image to display on the leading edge of the list item cell. If the image is larger than  , the list item scales down the image to maximum size. If you provide an animated image, the list item uses the first image in the animation sequence.
- `showsDisclosureIndicator`: A Boolean value that indicates whether the list item cell displays a disclosure indicator. Set to   to display the indicator on the trailing edge of the list item cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/init(text:detailtext:image:showsdisclosureindicator:))*