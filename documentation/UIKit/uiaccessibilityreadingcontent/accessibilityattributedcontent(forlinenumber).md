# accessibilityAttributedContent(forLineNumber:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the styled text associated with the specified line number.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func accessibilityAttributedContent(forLineNumber lineNumber: Int) -> NSAttributedString?
```

```objc
- (NSAttributedString *) accessibilityAttributedContentForLineNumber:(NSInteger) lineNumber;
```

#### Return Value

An attributed string containing the text that is associated with the specified line number, or `nil` if the line number is invalid. By default, this function returns `nil`.

#### Discussion

The system tries to call this method before calling the [`accessibilityContent(forLineNumber:)`](./accessibilitycontent%28forlinenumber%29.md) method.

## Parameters

- `lineNumber`: A line number in the receiver’s content.

## See Also

### Accessing the content on a page
- [func accessibilityLineNumber(for: CGPoint) -> Int](./accessibilitylinenumber%28for%29.md)
  Returns the line number that contains the specified point.
- [func accessibilityContent(forLineNumber: Int) -> String?](./accessibilitycontent%28forlinenumber%29.md)
  Returns the text associated with the specified line number.
- [func accessibilityFrame(forLineNumber: Int) -> CGRect](./accessibilityframe%28forlinenumber%29.md)
  Returns the onscreen frame associated with the specified line number.
- [func accessibilityAttributedPageContent() -> NSAttributedString?](./accessibilityattributedpagecontent%28%29.md)
  Returns the styled text displayed on the current page.
- [func accessibilityPageContent() -> String?](./accessibilitypagecontent%28%29.md)
  Returns the text displayed on the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent/accessibilityattributedcontent(forlinenumber:))*