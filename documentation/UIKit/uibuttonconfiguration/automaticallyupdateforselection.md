# automaticallyUpdateForSelection

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the style automatically updates when the button is in a selected state.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, assign, readwrite) BOOL automaticallyUpdateForSelection;
```

#### Discussion

The default value is [`true`](../../Swift/true.md) for the [`plainButtonConfiguration`](./plainbuttonconfiguration.md), [`grayButtonConfiguration`](./graybuttonconfiguration.md), and [`tintedButtonConfiguration`](./tintedbuttonconfiguration.md) configurations. Set this value to [`false`](../../Swift/false.md) to customize the selection behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibuttonconfiguration/automaticallyupdateforselection)*