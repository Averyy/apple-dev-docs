# accessoryView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An optional accessory view for the tab.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var accessoryView: NSView? { get set }
```

```objc
@property (strong, nullable) NSView * accessoryView;
```

#### Discussion

You can customize the window tab by adding an accessory view that displays alongside the tab’s title.

The [`translatesAutoresizingMaskIntoConstraints`](../nsview/translatesautoresizingmaskintoconstraints.md) property is automatically set to [`false`](../../Swift/false.md) on the view. Constraints can be created and activated to specify the view’s width and height values. A constraint is automatically added to vertically center the view, and to right align the view within the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowtab/accessoryview)*