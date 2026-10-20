# placeholderString

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The placeholder text for the cell, specified as a plain text string.

**Availability**:
- macOS

## Declaration

```swift
var placeholderString: String? { get set }
```

```objc
@property (copy, nullable) NSString * placeholderString;
```

#### Discussion

Assigning a new value to this property also clears out any value set for the [`placeholderAttributedString`](./placeholderattributedstring.md) property.

## See Also

### Managing Placeholder Strings
- [var placeholderAttributedString: NSAttributedString?](./placeholderattributedstring.md)
  The placeholder text for the cell, specified as an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfieldcell/placeholderstring)*