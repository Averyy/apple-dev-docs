# contentViewController

**Framework**: AppKit  
**Kind**: property

The view controller that manages the content of the popover.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@IBOutlet
@MainActor var contentViewController: NSViewController? { get set }
```

#### Discussion

You must set the content view controller of the popover before the popover is shown. Changes to the popover’s content view controller while the popover is shown will cause the popover to animate if the [`animates`](nspopover/animates.md) property is [`true`](https://developer.apple.com/documentation/Swift/true).

The default value is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/contentviewcontroller)*