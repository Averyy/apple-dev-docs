# accessibilityFrame(forLineNumber:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the onscreen frame associated with the specified line number.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func accessibilityFrame(forLineNumber lineNumber: Int) -> CGRect
```

#### Return Value

The frame in the receiver that contains the specified line number, in screen coordinates. By default, this method returns `CGRectZero`.

#### Discussion

To determine the onscreen rectangle (or frame) of a line, you can use code such as the following:

## Parameters

- `lineNumber`: The line number.

## See Also

- [static func convertToScreenCoordinates(CGRect, in: UIView) -> CGRect](uiaccessibility/converttoscreencoordinates(_:in:)-9ziiu.md)
  Converts the specified rectangle from view coordinates to screen coordinates.
- [func accessibilityLineNumber(for: CGPoint) -> Int](uiaccessibilityreadingcontent/accessibilitylinenumber(for:).md)
  Returns the line number that contains the specified point.
- [func accessibilityAttributedContent(forLineNumber: Int) -> NSAttributedString?](uiaccessibilityreadingcontent/accessibilityattributedcontent(forlinenumber:).md)
  Returns the styled text associated with the specified line number.
- [func accessibilityContent(forLineNumber: Int) -> String?](uiaccessibilityreadingcontent/accessibilitycontent(forlinenumber:).md)
  Returns the text associated with the specified line number.
- [func accessibilityAttributedPageContent() -> NSAttributedString?](uiaccessibilityreadingcontent/accessibilityattributedpagecontent.md)
  Returns the styled text displayed on the current page.
- [func accessibilityPageContent() -> String?](uiaccessibilityreadingcontent/accessibilitypagecontent.md)
  Returns the text displayed on the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent/accessibilityframe(forlinenumber:))*