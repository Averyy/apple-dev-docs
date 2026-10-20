# accessibilityAttributedPageContent()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSAttributedString *) accessibilityAttributedPageContent;
```

#### Return Value

An attributed string that contains the text displayed on the current page.

#### Discussion

The system tries to call this method before calling the [`accessibilityPageContent()`](./accessibilitypagecontent%28%29.md) method.

## See Also

### Accessing the content on a page
- [func accessibilityLineNumber(for: CGPoint) -> Int](./accessibilitylinenumber%28for%29.md)
  Returns the line number that contains the specified point.
- [func accessibilityAttributedContent(forLineNumber: Int) -> NSAttributedString?](./accessibilityattributedcontent%28forlinenumber%29.md)
  Returns the styled text associated with the specified line number.
- [func accessibilityContent(forLineNumber: Int) -> String?](./accessibilitycontent%28forlinenumber%29.md)
  Returns the text associated with the specified line number.
- [func accessibilityFrame(forLineNumber: Int) -> CGRect](./accessibilityframe%28forlinenumber%29.md)
  Returns the onscreen frame associated with the specified line number.
- [func accessibilityPageContent() -> String?](./accessibilitypagecontent%28%29.md)
  Returns the text displayed on the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent/accessibilityattributedpagecontent())*