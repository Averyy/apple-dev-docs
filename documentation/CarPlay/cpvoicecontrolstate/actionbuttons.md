# actionButtons

**Framework**: CarPlay  
**Kind**: property

An array of action buttons displayed in the template.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
var actionButtons: [CPButton] { get set }
```

#### Discussion

These buttons provide user interaction capabilities such as play/pause, favorite/unfavorite, share, or other content-specific actions. The buttons are displayed horizontally and are limited by maximumActionButtonCount.

Buttons should have clear, concise titles or recognizable icons. The order of buttons in the array determines their display order from leading to trailing in the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpvoicecontrolstate/actionbuttons)*