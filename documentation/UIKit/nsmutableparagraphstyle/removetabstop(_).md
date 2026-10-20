# removeTabStop(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Removes the first text tab with a location and type equal to the specified tab stop.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func removeTabStop(_ anObject: NSTextTab)
```

```objc
- (void) removeTabStop:(NSTextTab *) anObject;
```

## See Also

### Related Documentation
- [var tabStops: [NSTextTab]!](./tabstops.md)
  The text tab objects that represent the paragraph’s tab stops.
### Specifying tab information
- [func addTabStop(NSTextTab)](./addtabstop%28_%29.md)
  Adds the specified tab stop to the paragraph.
- [var tabStops: [NSTextTab]!](./tabstops.md)
  The text tab objects that represent the paragraph’s tab stops.
- [var defaultTabInterval: CGFloat](./defaulttabinterval.md)
  A number used as the document’s default tab spacing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/removetabstop(_:))*