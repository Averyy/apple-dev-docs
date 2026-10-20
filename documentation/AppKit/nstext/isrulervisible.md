# isRulerVisible

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver’s enclosing scroll view shows its ruler.

**Availability**:
- macOS

## Declaration

```swift
var isRulerVisible: Bool { get }
```

```objc
@property (readonly, getter=isRulerVisible) BOOL rulerVisible;
```

#### Discussion

[`true`](../../Swift/true.md) if the receiver’s enclosing scroll view shows its ruler, otherwise [`false`](../../Swift/false.md).

## See Also

### Using the ruler
- [func toggleRuler(Any?)](./toggleruler%28_%29.md)
  This action method shows or hides the ruler, if the receiver is enclosed in a scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/isrulervisible)*