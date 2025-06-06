# accessibilityLineNumber(for:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the line number that contains the specified point.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func accessibilityLineNumber(for point: CGPoint) -> Int
```

#### Return Value

The line number that contains the specified point or `NSNotFound` if the point indicates an empty area within the receiver’s rectangle. By default, this method returns `NSNotFound`.

#### Discussion

This method is called only when `point` is within the bounds of the view or element.

## Parameters

- `point`: A point within the bounds of the receiver’s view space, in screen coordinates. That is, a point for which  .

## See Also

- [static func convertToScreenCoordinates(CGRect, in: UIView) -> CGRect](uiaccessibility/converttoscreencoordinates(_:in:)-9ziiu.md)
  Converts the specified rectangle from view coordinates to screen coordinates.
- [func accessibilityAttributedContent(forLineNumber: Int) -> NSAttributedString?](uiaccessibilityreadingcontent/accessibilityattributedcontent(forlinenumber:).md)
  Returns the styled text associated with the specified line number.
- [func accessibilityContent(forLineNumber: Int) -> String?](uiaccessibilityreadingcontent/accessibilitycontent(forlinenumber:).md)
  Returns the text associated with the specified line number.
- [func accessibilityFrame(forLineNumber: Int) -> CGRect](uiaccessibilityreadingcontent/accessibilityframe(forlinenumber:).md)
  Returns the onscreen frame associated with the specified line number.
- [func accessibilityAttributedPageContent() -> NSAttributedString?](uiaccessibilityreadingcontent/accessibilityattributedpagecontent.md)
  Returns the styled text displayed on the current page.
- [func accessibilityPageContent() -> String?](uiaccessibilityreadingcontent/accessibilitypagecontent.md)
  Returns the text displayed on the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent/accessibilitylinenumber(for:))*