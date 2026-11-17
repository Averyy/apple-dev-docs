# mapButtonSafeAreaLayoutGuide

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A layout guide that represents the portion of the window unobscured by other content.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var mapButtonSafeAreaLayoutGuide: UILayoutGuide { get }
```

```objc
@property (nonatomic, readonly) UILayoutGuide * mapButtonSafeAreaLayoutGuide;
```

## Discussion

The [`CPMapTemplate`](../cpmaptemplate.md) type adds buttons and other content to your navigation interface. When displaying map content in your custom view controller, this layout guide defines the area not covered by that other content. Use this guide to position map-related content that needs to remain visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpwindow/mapbuttonsafearealayoutguide)*