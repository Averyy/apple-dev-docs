# accessibilityContent(forLineNumber:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the text associated with the specified line number.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@MainActor
func accessibilityContent(forLineNumber lineNumber: Int) -> String?
```

```objc
- (NSString *) accessibilityContentForLineNumber:(NSInteger) lineNumber;
```

## Return Value

A string containing the text that is associated with the specified line number, or `nil` if the line number is invalid. By default, this function returns `nil`.

## Discussion

The system tries to call the [`accessibilityAttributedContent(forLineNumber:)`](./accessibilityattributedcontent%28forlinenumber%29.md) method before calling this method.

## Parameters

- `lineNumber`: A line number in the receiver’s content.

## See Also

### Accessing the content on a page
- [func accessibilityLineNumber(for: CGPoint) -> Int](./accessibilitylinenumber%28for%29.md)
  Returns the line number that contains the specified point.
- [func accessibilityAttributedContent(forLineNumber: Int) -> NSAttributedString?](./accessibilityattributedcontent%28forlinenumber%29.md)
  Returns the styled text associated with the specified line number.
- [func accessibilityFrame(forLineNumber: Int) -> CGRect](./accessibilityframe%28forlinenumber%29.md)
  Returns the onscreen frame associated with the specified line number.
- [func accessibilityAttributedPageContent() -> NSAttributedString?](./accessibilityattributedpagecontent%28%29.md)
  Returns the styled text displayed on the current page.
- [func accessibilityPageContent() -> String?](./accessibilitypagecontent%28%29.md)
  Returns the text displayed on the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent/accessibilitycontent(forlinenumber:))*