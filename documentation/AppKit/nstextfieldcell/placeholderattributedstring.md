# placeholderAttributedString

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The placeholder text for the cell, specified as an attributed string.

**Availability**:
- macOS

## Declaration

```swift
@NSCopying
var placeholderAttributedString: NSAttributedString? { get set }
```

```objc
@property (copy, nullable) NSAttributedString * placeholderAttributedString;
```

## Discussion

Assigning a new value to this property also clears out any value set for the [`placeholderString`](./placeholderstring.md) property.

## See Also

### Managing Placeholder Strings
- [var placeholderString: String?](./placeholderstring.md)
  The placeholder text for the cell, specified as a plain text string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfieldcell/placeholderattributedstring)*