# accessibilityPageContent()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the text displayed on the current page.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@MainActor
func accessibilityPageContent() -> String?
```

```objc
- (NSString *) accessibilityPageContent;
```

#### Return Value

A string that contains the text displayed on the current page.

#### Discussion

The system tries to call the [`accessibilityAttributedPageContent()`](./accessibilityattributedpagecontent%28%29.md) method before calling this method.

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
- [func accessibilityAttributedPageContent() -> NSAttributedString?](./accessibilityattributedpagecontent%28%29.md)
  Returns the styled text displayed on the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent/accessibilitypagecontent())*