# removeTabStop(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the first text tab with a location and type equal to the specified tab stop.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func removeTabStop(_ anObject: NSTextTab)
```

```objc
- (void) removeTabStop:(NSTextTab *) anObject;
```

## See Also

### Specifying tab information
- [func addTabStop(NSTextTab)](./addtabstop%28_%29.md)
  Adds the specified tab stop to the paragraph.
- [var tabStops: [NSTextTab]!](./tabstops.md)
  The text tab objects that represent the paragraph’s tab stops.
- [var defaultTabInterval: CGFloat](./defaulttabinterval.md)
  A number used as the document’s default tab spacing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/removetabstop(_:))*