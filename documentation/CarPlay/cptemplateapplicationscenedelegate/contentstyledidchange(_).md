# contentStyleDidChange(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells your app that the suggested content style for this scene changed.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
optional func contentStyleDidChange(_ contentStyle: UIUserInterfaceStyle)
```

```objc
- (void) contentStyleDidChange:(UIUserInterfaceStyle) contentStyle;
```

## Discussion

Refresh your app’s interface as needed to match the specified content style. For more information about managing interface style changes for your content, see [Supporting Dark Mode in your interface](../../UIKit/supporting-dark-mode-in-your-interface.md).

## Parameters

- `contentStyle`: The new content style to apply to your interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscenedelegate/contentstyledidchange(_:))*