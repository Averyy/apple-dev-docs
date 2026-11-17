# init(lightContentImage:darkContentImage:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates an image set with light and dark versions of an image.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(lightContentImage lightImage: UIImage, darkContentImage darkImage: UIImage)
```

```objc
- (instancetype) initWithLightContentImage:(UIImage *) lightImage darkContentImage:(UIImage *) darkImage;
```

## Return Value

A newly initialized image set.

## Parameters

- `lightImage`: The image the system displays for an image set when [`userInterfaceStyle`](../../UIKit/uitraitcollection/userinterfacestyle.md) is [`UIUserInterfaceStyle.light`](../../UIKit/uiuserinterfacestyle/light.md).
- `darkImage`: The image the system displays for an image set when [`userInterfaceStyle`](../../UIKit/uitraitcollection/userinterfacestyle.md) is [`UIUserInterfaceStyle.dark`](../../UIKit/uiuserinterfacestyle/dark.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpimageset/init(lightcontentimage:darkcontentimage:))*