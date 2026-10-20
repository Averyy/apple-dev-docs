# init(coder:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a new line fragment with from data in an unarchiver.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
init?(coder aDecoder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) aDecoder;
```

## Parameters

- `aDecoder`: A decoder that conforms to the [`NSCoder`](../../Foundation/nscoder.md) protocol.

## See Also

### Creating line fragments
- [init(attributedString: NSAttributedString, range: NSRange)](./init%28attributedstring,range%29.md)
  Creates a new line fragment from the attributed string for the range of characters you specify.
- [convenience init(string: String, attributes: [NSAttributedString.Key : Any], range: NSRange)](./init%28string,attributes,range%29.md)
  Creates a new line fragment using the string, attributes, and range you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlinefragment/init(coder:))*