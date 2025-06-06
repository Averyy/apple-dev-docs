# accessibilityPageContent()

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the text displayed on the current page.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func accessibilityPageContent() -> String?
```

#### Return Value

A string that contains the text displayed on the current page.

#### Discussion

The system tries to call the [`accessibilityAttributedPageContent()`](uiaccessibilityreadingcontent/accessibilityattributedpagecontent().md) method before calling this method.

## See Also

- [func accessibilityLineNumber(for: CGPoint) -> Int](uiaccessibilityreadingcontent/accessibilitylinenumber(for:).md)
  Returns the line number that contains the specified point.
- [func accessibilityAttributedContent(forLineNumber: Int) -> NSAttributedString?](uiaccessibilityreadingcontent/accessibilityattributedcontent(forlinenumber:).md)
  Returns the styled text associated with the specified line number.
- [func accessibilityContent(forLineNumber: Int) -> String?](uiaccessibilityreadingcontent/accessibilitycontent(forlinenumber:).md)
  Returns the text associated with the specified line number.
- [func accessibilityFrame(forLineNumber: Int) -> CGRect](uiaccessibilityreadingcontent/accessibilityframe(forlinenumber:).md)
  Returns the onscreen frame associated with the specified line number.
- [func accessibilityAttributedPageContent() -> NSAttributedString?](uiaccessibilityreadingcontent/accessibilityattributedpagecontent.md)
  Returns the styled text displayed on the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent/accessibilitypagecontent())*