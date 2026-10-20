# placeholderString

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The cell’s plain text placeholder string.

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

If this property returns `nil`, you can also call `placeholderAttributedString` to see if the cell has an attributed placeholder string. Note that invoking this method clears out any attributed string set by the [`placeholderAttributedString`](./placeholderattributedstring.md) property.

## See Also

### Asking About Placeholder Values
- [var placeholderAttributedString: NSAttributedString?](./placeholderattributedstring.md)
  The cell’s attributed placeholder string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsformcell/placeholderstring)*