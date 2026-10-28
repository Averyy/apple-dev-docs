# init(identifier:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes a newly created table column with a string identifier.

**Availability**:
- macOS

## Declaration

```swift
init(identifier: NSUserInterfaceItemIdentifier)
```

```objc
- (instancetype) initWithIdentifier:(NSUserInterfaceItemIdentifier) identifier;
```

## Return Value

An initialized table column instance with an [`NSTextFieldCell`](../nstextfieldcell.md) instance as its default cell.

## Discussion

You can set the table column title using the [`title`](./title.md) property.

This method is the designated initializer for the `NSTableColumn` class.

## Parameters

- `identifier`: The string identifier for the column.

## See Also

### Related Documentation
- [class NSTableView](../nstableview.md)
  A set of related records, displayed in rows that represent individual records and columns that represent the attributes of those records.
- [var identifier: NSUserInterfaceItemIdentifier](./identifier.md)
  The identifier string for the table column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/init(identifier:))*