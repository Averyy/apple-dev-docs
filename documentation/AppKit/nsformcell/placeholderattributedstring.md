# placeholderAttributedString

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The cell’s attributed placeholder string.

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

#### Discussion

If this property returns `nil`, you can also call `placeholderString` to see if the cell has a plain text placeholder string.

## See Also

### Asking About Placeholder Values
- [var placeholderString: String?](./placeholderstring.md)
  The cell’s plain text placeholder string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsformcell/placeholderattributedstring)*