# init(attributedString:range:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a new line fragment from the attributed string for the range of characters you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
init(attributedString: NSAttributedString, range: NSRange)
```

```objc
- (instancetype) initWithAttributedString:(NSAttributedString *) attributedString range:(NSRange) range;
```

## Parameters

- `attributedString`: The attributed string.
- `range`: An [`NSRange`](../../Foundation/nsrange-c.struct.md) that specifies which characters to include.

## See Also

### Creating line fragments
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a new line fragment with from data in an unarchiver.
- [convenience init(string: String, attributes: [NSAttributedString.Key : Any], range: NSRange)](./init%28string,attributes,range%29.md)
  Creates a new line fragment using the string, attributes, and range you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlinefragment/init(attributedstring:range:))*