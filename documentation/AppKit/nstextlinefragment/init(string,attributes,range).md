# init(string:attributes:range:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a new line fragment using the string, attributes, and range you provide.

**Availability**:
- macOS 12.0+

## Declaration

```swift
convenience init(string: String, attributes: [NSAttributedString.Key : Any] = [:], range: NSRange)
```

```objc
- (instancetype) initWithString:(NSString *) string attributes:(NSDictionary<NSString *,id> *) attributes range:(NSRange) range;
```

## Parameters

- `string`: An attributed string.
- `attributes`: A dictionary of attributes.
- `range`: The range to use from `string`.

## See Also

### Creating line fragments
- [init(attributedString: NSAttributedString, range: NSRange)](./init%28attributedstring,range%29.md)
  Creates a new line fragment from the attributed string for the range of characters you specify.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a new line fragment with from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlinefragment/init(string:attributes:range:))*