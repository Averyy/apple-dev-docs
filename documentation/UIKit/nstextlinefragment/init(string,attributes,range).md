# init(string:attributes:range:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a new line fragment using the string, attributes, and range you provide.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlinefragment/init(string:attributes:range:))*