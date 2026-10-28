# usesInspectorBar

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether this text view uses the inspector bar.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var usesInspectorBar: Bool { get set }
```

```objc
@property BOOL usesInspectorBar;
```

## Discussion

The inspector bar displays text formatting controls, much like those in iWork applications, which can be used in place of the formatting controls in the ruler accessory view.

## See Also

### Using text formatting controls
- [var usesRuler: Bool](./usesruler.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager use a ruler.
- [var isRulerVisible: Bool](./isrulervisible.md)
  A Boolean value that controls whether the scroll view enclosing text views sharing the receiver’s layout manager displays the ruler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/usesinspectorbar)*