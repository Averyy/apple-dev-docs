# accessibilityAttributedPageContent()

**Framework**: UIKit  
**Kind**: method

Returns the styled text displayed on the current page.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func accessibilityAttributedPageContent() -> NSAttributedString?
```

#### Return Value

An attributed string that contains the text displayed on the current page.

#### Discussion

The system tries to call this method before calling the [`accessibilityPageContent()`](uiaccessibilityreadingcontent/accessibilitypagecontent().md) method.

## See Also

- [func accessibilityLineNumber(for: CGPoint) -> Int](uiaccessibilityreadingcontent/accessibilitylinenumber(for:).md)
  Returns the line number that contains the specified point.
- [func accessibilityAttributedContent(forLineNumber: Int) -> NSAttributedString?](uiaccessibilityreadingcontent/accessibilityattributedcontent(forlinenumber:).md)
  Returns the styled text associated with the specified line number.
- [func accessibilityContent(forLineNumber: Int) -> String?](uiaccessibilityreadingcontent/accessibilitycontent(forlinenumber:).md)
  Returns the text associated with the specified line number.
- [func accessibilityFrame(forLineNumber: Int) -> CGRect](uiaccessibilityreadingcontent/accessibilityframe(forlinenumber:).md)
  Returns the onscreen frame associated with the specified line number.
- [func accessibilityPageContent() -> String?](uiaccessibilityreadingcontent/accessibilitypagecontent.md)
  Returns the text displayed on the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent/accessibilityattributedpagecontent())*