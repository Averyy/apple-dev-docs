# contentViewController

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The view controller that manages the content of the popover.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@IBOutlet
var contentViewController: NSViewController? { get set }
```

```objc
@property (retain, nullable) NSViewController * contentViewController;
```

## Discussion

You must set the content view controller of the popover before the popover is shown. Changes to the popover’s content view controller while the popover is shown will cause the popover to animate if the [`animates`](./animates.md) property is [`true`](../../Swift/true.md).

The default value is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/contentviewcontroller)*