# init(string:attributes:range:)

**Framework**: AppKit  
**Kind**: init

Creates a new line fragment using the string, attributes, and range you provide.

**Availability**:
- macOS 12.0+

## Declaration

```swift
convenience init(string: String, attributes: [NSAttributedString.Key : Any] = [:], range: NSRange)
```

## Parameters

- `string`: An attributed string.
- `attributes`: A dictionary of attributes.
- `range`: The range to use from  .

## See Also

- [init(attributedString: NSAttributedString, range: NSRange)](nstextlinefragment/init(attributedstring:range:).md)
  Creates a new line fragment from the attributed string for the range of characters you specify.
- [init?(coder: NSCoder)](nstextlinefragment/init(coder:).md)
  Creates a new line fragment with from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlinefragment/init(string:attributes:range:))*