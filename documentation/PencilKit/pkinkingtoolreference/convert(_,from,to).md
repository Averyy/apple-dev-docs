# convert(_:from:to:)

**Framework**: PencilKit  
**Kind**: method  
**Role**: Type Method

Converts a color from one user interface style to another.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func convert(_ color: UIColor, from fromUserInterfaceStyle: UIUserInterfaceStyle, to toUserInterfaceStyle: UIUserInterfaceStyle) -> UIColor
```

```objc
+ (UIColor *) convertColor:(UIColor *) color fromUserInterfaceStyle:(UIUserInterfaceStyle) fromUserInterfaceStyle to:(UIUserInterfaceStyle) toUserInterfaceStyle;
```

## Parameters

- `color`: The color to convert.
- `fromUserInterfaceStyle`: The user interface style to convert the color from.
- `toUserInterfaceStyle`: The user interface style to convert the color to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkingtoolreference/convert(_:from:to:))*