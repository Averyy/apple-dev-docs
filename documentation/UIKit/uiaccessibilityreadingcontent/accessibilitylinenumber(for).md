# accessibilityLineNumber(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the line number that contains the specified point.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@MainActor
func accessibilityLineNumber(for point: CGPoint) -> Int
```

```objc
- (NSInteger) accessibilityLineNumberForPoint:(CGPoint) point;
```

## Return Value

The line number that contains the specified point or `NSNotFound` if the point indicates an empty area within the receiver’s rectangle. By default, this method returns `NSNotFound`.

## Discussion

This method is called only when `point` is within the bounds of the view or element.

## Parameters

- `point`: A point within the bounds of the receiver’s view space, in screen coordinates. That is, a point for which `[self pointInside:point withEvent:event] == YES`.

## See Also

### Related Documentation
- [static func convertToScreenCoordinates(CGRect, in: UIView) -> CGRect](../uiaccessibility/converttoscreencoordinates%28_,in%29-9ziiu.md)
  Converts the specified rectangle from view coordinates to screen coordinates.
### Accessing the content on a page
- [func accessibilityAttributedContent(forLineNumber: Int) -> NSAttributedString?](./accessibilityattributedcontent%28forlinenumber%29.md)
  Returns the styled text associated with the specified line number.
- [func accessibilityContent(forLineNumber: Int) -> String?](./accessibilitycontent%28forlinenumber%29.md)
  Returns the text associated with the specified line number.
- [func accessibilityFrame(forLineNumber: Int) -> CGRect](./accessibilityframe%28forlinenumber%29.md)
  Returns the onscreen frame associated with the specified line number.
- [func accessibilityAttributedPageContent() -> NSAttributedString?](./accessibilityattributedpagecontent%28%29.md)
  Returns the styled text displayed on the current page.
- [func accessibilityPageContent() -> String?](./accessibilitypagecontent%28%29.md)
  Returns the text displayed on the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent/accessibilitylinenumber(for:))*