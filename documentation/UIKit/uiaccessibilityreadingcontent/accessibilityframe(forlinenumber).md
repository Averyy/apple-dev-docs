# accessibilityFrame(forLineNumber:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the onscreen frame associated with the specified line number.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@MainActor
func accessibilityFrame(forLineNumber lineNumber: Int) -> CGRect
```

```objc
- (CGRect) accessibilityFrameForLineNumber:(NSInteger) lineNumber;
```

#### Return Value

The frame in the receiver that contains the specified line number, in screen coordinates. By default, this method returns `CGRectZero`.

#### Discussion

To determine the onscreen rectangle (or frame) of a line, you can use code such as the following:

**Swift**:

```swift
let lineBounds: CGRect = // the bounds of the line in view space
let view: UIView = // the relevant view
return UIAccessibilityConvertFrameToScreenCoordinates(lineBounds, view)
```

**Objective-C**:

```objc
CGRect lineBounds = // The bounds of the line in view space.
UIView *view = // The relevant view.
return UIAccessibilityConvertFrameToScreenCoordinates(lineBounds, view);
```

## Parameters

- `lineNumber`: The line number.

## See Also

### Related Documentation
- [static func convertToScreenCoordinates(CGRect, in: UIView) -> CGRect](../uiaccessibility/converttoscreencoordinates%28_,in%29-9ziiu.md)
  Converts the specified rectangle from view coordinates to screen coordinates.
### Accessing the content on a page
- [func accessibilityLineNumber(for: CGPoint) -> Int](./accessibilitylinenumber%28for%29.md)
  Returns the line number that contains the specified point.
- [func accessibilityAttributedContent(forLineNumber: Int) -> NSAttributedString?](./accessibilityattributedcontent%28forlinenumber%29.md)
  Returns the styled text associated with the specified line number.
- [func accessibilityContent(forLineNumber: Int) -> String?](./accessibilitycontent%28forlinenumber%29.md)
  Returns the text associated with the specified line number.
- [func accessibilityAttributedPageContent() -> NSAttributedString?](./accessibilityattributedpagecontent%28%29.md)
  Returns the styled text displayed on the current page.
- [func accessibilityPageContent() -> String?](./accessibilitypagecontent%28%29.md)
  Returns the text displayed on the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent/accessibilityframe(forlinenumber:))*