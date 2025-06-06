# findBarContainer

**Framework**: AppKit  
**Kind**: property

Specifies the find bar container.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@IBOutlet
unowned(unsafe) var findBarContainer: (any NSTextFinderBarContainer)? { get set }
```

#### Discussion

This property must be set to support the find bar.

When the find bar is to be shown, `NSTextFinder` invokes `showFindBarView:` on the `findBarContainer` object, passing the view for the find bar, which it should display somewhere that is associated appropriately with the content being searched.

The `NSScrollView` class implements `NSTextFinderBarContainer` protocol and is the correct place to display the find bar in most circumstances. The container may freely modify the find bar view’s width and origin, but not its height.

If this property is not set, then the find bar cannot be shown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinder/findbarcontainer)*