# showsSelectionIndicator

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the selection indicator is displayed.

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: In iOS 7 and later, you can’t customize the picker view’s selection indicator. The selection indicator is always shown, so setting this property to [`false`](../../Swift/false.md) has no effect.

## Declaration

```swift
var showsSelectionIndicator: Bool { get set }
```

```objc
@property (nonatomic) BOOL showsSelectionIndicator;
```

#### Discussion

If the value of the property is [`true`](../../Swift/true.md), the picker view shows a clear overlay across the current row. The default value of this property is [`false`](../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerview/showsselectionindicator)*