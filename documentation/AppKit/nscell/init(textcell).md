# init(textCell:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns an NSCell object initialized with the specified string and set to have the cell’s default menu.

**Availability**:
- macOS

## Declaration

```swift
init(textCell string: String)
```

```objc
- (instancetype) initTextCell:(NSString *) string;
```

#### Return Value

An initialized `NSCell` object, or `nil` if the cell could not be initialized.

#### Discussion

If no field editor (a shared [`NSText`](../nstext.md) object) has been created for all `NSCell` objects, one is created.

This is one of four designated initializers you must implement when subclassing. See [Designated Initializers](../nscell.md#Designated-Initializers) for the complete list.

## Parameters

- `string`: The initial string to use for the cell.

## See Also

### Initializing a Cell
- [init(imageCell: NSImage?)](./init%28imagecell%29.md)
  Returns an `NSCell` object initialized with the specified image and set to have the cell’s default menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/init(textcell:))*