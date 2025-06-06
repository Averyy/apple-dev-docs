# init(textCell:)

**Framework**: AppKit  
**Kind**: init

Returns an `NSFormCell` object initialized with the specified title string.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
init(textCell string: String?)
```

#### Return Value

An initialized `NSFormCell` object.

#### Discussion

The contents of the cell’s editable text entry field are set to the empty string (`@""`). The font for both title and text is the user’s chosen system font in 12.0 point, and the text area is drawn with a bezel. This method is the designated initializer for the `NSFormCell` class.

## Parameters

- `string`: The title for the new form cell object.

## See Also

- [Form Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Form/Form.html#//apple_ref/doc/uid/10000021i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsformcell/init(textcell:))*