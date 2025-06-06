# contentType

**Framework**: AppKit  
**Kind**: property  
**Required**: Yes

The semantic meaning for a text input area.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var contentType: NSTextContentType? { get set }
```

#### Discussion

Use this property to give the system information about the expected semantic meaning for the content that people enter. For example, you might specify [`emailAddress`](nstextcontenttype/emailaddress.md) for a text field that people fill in to receive an email confirmation.

For possible values you can use, see [`NSTextContentType`](nstextcontenttype.md); by default, the value of this property is `nil`.

## See Also

- [struct NSTextContentType](nstextcontenttype.md)
  Constants that identify the semantic meaning for a text-entry area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontent/contenttype)*