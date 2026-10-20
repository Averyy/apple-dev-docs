# addTabStop(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds the specified tab stop to the paragraph.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func addTabStop(_ anObject: NSTextTab)
```

```objc
- (void) addTabStop:(NSTextTab *) anObject;
```

## See Also

### Specifying tab information
- [func removeTabStop(NSTextTab)](./removetabstop%28_%29.md)
  Removes the first text tab with a location and type equal to the specified tab stop.
- [var tabStops: [NSTextTab]!](./tabstops.md)
  The text tab objects that represent the paragraph’s tab stops.
- [var defaultTabInterval: CGFloat](./defaulttabinterval.md)
  A number used as the document’s default tab spacing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/addtabstop(_:))*