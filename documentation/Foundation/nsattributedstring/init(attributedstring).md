# init(attributedString:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a new attributed string from the contents of another attributed string.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(attributedString attrStr: NSAttributedString)
```

```objc
- (instancetype) initWithAttributedString:(NSAttributedString *) attrStr;
```

#### Return Value

An [`NSAttributedString`](../nsattributedstring.md) object initialized with the characters and attributes of `attrStr`.

## Parameters

- `attrStr`: An attributed string.

## See Also

### Related Documentation
- [init?(RTF: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./init%28rtf,documentattributes%29.md)
  Creates an attributed string by decoding the stream of RTF commands and data in the specified data object.
### Creating from another string
- [init(string: String)](./init%28string%29.md)
  Creates an attributed string with the specified text and no attribute information.
- [init(string: String, attributes: [NSAttributedString.Key : Any]?)](./init%28string,attributes%29.md)
  Creates an attributed string with the specified text and attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(attributedstring:))*