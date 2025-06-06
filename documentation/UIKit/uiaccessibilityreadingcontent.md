# UIAccessibilityReadingContent

**Framework**: UIKit  
**Kind**: protocol

Methods to implement for an object that represents content that users read, such as a book or an article.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol UIAccessibilityReadingContent
```

#### Overview

To give VoiceOver users a superior, continuous reading experience, you can implement this protocol on an element that represents readable content, characterize it with the [`causesPageTurn`](uiaccessibilitytraits/causespageturn.md) trait, and use the [`UIAccessibilityScrollDirection.next`](uiaccessibilityscrolldirection/next.md) and [`UIAccessibilityScrollDirection.previous`](uiaccessibilityscrolldirection/previous.md) constants to enable page turning.

## Topics

### Accessing the content on a page
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
- [func accessibilityPageContent() -> String?](uiaccessibilityreadingcontent/accessibilitypagecontent.md)
  Returns the text displayed on the current page.

## See Also

- [UIAccessibilityFocus](../ObjectiveC/uiaccessibilityfocus.md)
  An informal protocol that provides a way to determine whether an assistive app, such as VoiceOver, has focus on an accessible element.
- [protocol UIAccessibilityIdentification](uiaccessibilityidentification.md)
  Methods that associate a unique identifier with elements in your user interface.
- [protocol UIAccessibilityContentSizeCategoryImageAdjusting](uiaccessibilitycontentsizecategoryimageadjusting.md)
  Methods to determine when to adjust images for different content size categories.
- [struct UIAccessibilityTextualContext](uiaccessibilitytextualcontext.md)
  Constants that describe a named context that helps identify and classify the type of text inside an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent)*