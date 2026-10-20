# addTabStop(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds the specified tab stop to the paragraph.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addTabStop(_ anObject: NSTextTab)
```

```objc
- (void) addTabStop:(NSTextTab *) anObject;
```

## See Also

### Related Documentation
- [var tabStops: [NSTextTab]!](./tabstops.md)
  The text tab objects that represent the paragraph’s tab stops.
### Specifying tab information
- [func removeTabStop(NSTextTab)](./removetabstop%28_%29.md)
  Removes the first text tab with a location and type equal to the specified tab stop.
- [var tabStops: [NSTextTab]!](./tabstops.md)
  The text tab objects that represent the paragraph’s tab stops.
- [var defaultTabInterval: CGFloat](./defaulttabinterval.md)
  A number used as the document’s default tab spacing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/addtabstop(_:))*