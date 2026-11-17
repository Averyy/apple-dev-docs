# init(trailingItem:trailingImage:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates the configuration object with the items to display at the leading edge of the row.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(trailingItem: CPMessageTrailingItem, trailingImage: UIImage?)
```

```objc
- (instancetype) initWithTrailingItem:(CPMessageTrailingItem) trailingItem trailingImage:(UIImage *) trailingImage;
```

## Return Value

An initialized configuration object.

## Parameters

- `trailingItem`: A standard system symbol to display. Specify [`CPMessageTrailingItem.none`](../cpmessagetrailingitem/none.md) if you don’t want to display a standard symbol.
- `trailingImage`: A custom image you provide. If the image originates from an asset catalog, CarPlay manages light and dark variants of your image and switches them when needed. If you specify an image larger or smaller than the value in [`CPMaximumMessageItemImageSize`](../cpmaximummessageitemimagesize.md), the initializer scales the image to that size. If the image contains an animated sequence, CarPlay shows only the first image in the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitemtrailingconfiguration/init(trailingitem:trailingimage:))*