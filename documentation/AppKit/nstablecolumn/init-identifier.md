# init(identifier:)

**Framework**: AppKit  
**Kind**: init

Initializes a newly created table column with a string identifier.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
init(identifier: NSUserInterfaceItemIdentifier)
```

#### Return Value

An initialized table column instance with an [`NSTextFieldCell`](nstextfieldcell.md) instance as its default cell.

#### Discussion

You can set the table column title using the [`title`](nstablecolumn/title.md) property.

This method is the designated initializer for the `NSTableColumn` class.

## Parameters

- `identifier`: The string identifier for the column.

## See Also

- [Table View Programming Guide for Mac](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TableView/Introduction/Introduction.html#//apple_ref/doc/uid/10000026i)
- [var identifier: NSUserInterfaceItemIdentifier](nstablecolumn/identifier.md)
  The identifier string for the table column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/init(identifier:))*