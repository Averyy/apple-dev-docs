# state

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The layout information state.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var state: NSTextLayoutFragment.State { get }
```

```objc
@property (readonly) NSTextLayoutFragmentState state;
```

## Discussion

This property is KVO-compliant.

## See Also

### Getting element information
- [NSTextLayoutFragment.State](./state-swift.enum.md)
  Values that describe the possible layout states.
- [var rangeInElement: NSTextRange](./rangeinelement.md)
  The range inside the text element relative to the document origin.
- [var textElement: NSTextElement?](./textelement.md)
  The parent text element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutfragment/state-swift.property)*