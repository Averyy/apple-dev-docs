# init(string:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates an attributed string with the specified text and no attribute information.

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
init(string str: String)
```

```objc
- (instancetype) initWithString:(NSString *) str;
```

#### Return Value

An [`NSAttributedString`](../nsattributedstring.md) object initialized with the characters of `str` and no attribute information.

## Parameters

- `str`: The text for the new attributed string.

## See Also

### Related Documentation
- [init?(RTF: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./init%28rtf,documentattributes%29.md)
  Creates an attributed string by decoding the stream of RTF commands and data in the specified data object.
- [Attributed String Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AttributedStrings/AttributedStrings.html#//apple_ref/doc/uid/10000036i)
### Creating from another string
- [init(string: String, attributes: [NSAttributedString.Key : Any]?)](./init%28string,attributes%29.md)
  Creates an attributed string with the specified text and attributes.
- [init(attributedString: NSAttributedString)](./init%28attributedstring%29.md)
  Creates a new attributed string from the contents of another attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(string:))*