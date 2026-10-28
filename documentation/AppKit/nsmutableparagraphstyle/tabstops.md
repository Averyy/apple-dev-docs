# tabStops

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The text tab objects that represent the paragraph’s tab stops.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var tabStops: [NSTextTab]! { get set }
```

```objc
@property (copy, null_resettable) NSArray<NSTextTab *> * tabStops;
```

## Discussion

The [`NSTextTab`](../nstexttab.md) objects, sorted by location, define the tab stops for the paragraph style. The default value is an array of 12 left-aligned tabs at 28-point intervals.

## See Also

### Specifying tab information
- [func addTabStop(NSTextTab)](./addtabstop%28_%29.md)
  Adds the specified tab stop to the paragraph.
- [func removeTabStop(NSTextTab)](./removetabstop%28_%29.md)
  Removes the first text tab with a location and type equal to the specified tab stop.
- [var defaultTabInterval: CGFloat](./defaulttabinterval.md)
  A number used as the document’s default tab spacing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/tabstops)*