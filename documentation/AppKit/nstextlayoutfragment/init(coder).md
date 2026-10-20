# init(coder:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a new layout fragment with the coder you provide.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## Parameters

- `coder`: A coder that conforms to [`NSCoder`](../../Foundation/nscoder.md).

## See Also

### Creating a layout fragment
- [init(textElement: NSTextElement, range: NSTextRange?)](./init%28textelement,range%29.md)
  Create a new layout fragment using the provided text element and range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutfragment/init(coder:))*