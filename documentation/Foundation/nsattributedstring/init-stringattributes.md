# init(string:attributes:)

**Framework**: Foundation  
**Kind**: init

Creates an attributed string with the specified text and attributes.

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
init(string str: String, attributes attrs: [NSAttributedString.Key : Any]? = nil)
```

#### Discussion

Returns an [`NSAttributedString`](nsattributedstring.md) object initialized with the characters of `str` and the attributes of `attrs`.

## Parameters

- `str`: The text for the new attributed string.
- `attrs`: The attributes for the new attributed string. This method applies the attributes to the entire string. For a list of attributes that you can include in this dictionary, see  .

## See Also

- [init?(RTF: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(rtf:documentattributes:).md)
  Creates an attributed string by decoding the stream of RTF commands and data in the specified data object.
- [init(string: String)](nsattributedstring/init(string:).md)
  Creates an attributed string with the specified text and no attribute information.
- [init(attributedString: NSAttributedString)](nsattributedstring/init(attributedstring:).md)
  Creates a new attributed string from the contents of another attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(string:attributes:))*