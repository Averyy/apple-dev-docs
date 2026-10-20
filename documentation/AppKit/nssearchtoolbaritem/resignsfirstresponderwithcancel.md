# resignsFirstResponderWithCancel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that enables the cancel button in the search field to resign the first responder in addition to clearing the contents.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var resignsFirstResponderWithCancel: Bool { get set }
```

```objc
@property BOOL resignsFirstResponderWithCancel;
```

#### Discussion

The default value is `true`. If set to `false`, the cancel button only clears the contents of the search field.

## See Also

### Configuring a search item
- [var preferredWidthForSearchField: CGFloat](./preferredwidthforsearchfield.md)
  The preferred width for the toolbar item when it has keyboard focus.
- [var searchField: NSSearchField](./searchfield.md)
  The search field inside the toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchtoolbaritem/resignsfirstresponderwithcancel)*