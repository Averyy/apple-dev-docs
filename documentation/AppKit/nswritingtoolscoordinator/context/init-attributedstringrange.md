# init(attributedString:range:)

**Framework**: AppKit  
**Kind**: init

Creates a context object with the specified attributed string and range information.

**Availability**:
- macOS 15.2+

## Declaration

```swift
init(attributedString: NSAttributedString, range: NSRange)
```

#### Discussion

When Writing Tools asks for your view’s current selection, it’s best to create a string that includes text before and after that selection. During the evaluation process, Writing Tools can use the additional text you provided to improve the results it delivers. If you do provide additional text, set the `range` parameter to the portion of `attributedString` with the current selection. Don’t use the `range` parameter to specify the location of the text in your view’s text storage.

## Parameters

- `attributedString`: A string that contains some or all of the content   from your view’s text storage. This initializer makes a copy of the   string you provide, so you can discard the original when you’re done.
- `range`: The portion of   you want Writing Tools to   evaluate. If you want Writing Tools to evaluate the entire string you   provided, specify a range with a location of   and a length equal to   your string’s length. If you want Writing Tools to evaluate only part   of the string, provide the appropriate range in this parameter. Writing   Tools suggests changes only to the range of text you specify, but it   can consider text outside that range during the evaluation process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/context/init(attributedstring:range:))*