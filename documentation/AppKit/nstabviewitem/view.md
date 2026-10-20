# view

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Sets the view associated with the receiver to `view`.

**Availability**:
- macOS

## Declaration

```swift
var view: NSView? { get set }
```

```objc
@property (strong, nullable) NSView * view;
```

#### Discussion

This is the view displayed when a user clicks the tab. When you set a new view, the old view is released.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewitem/view)*