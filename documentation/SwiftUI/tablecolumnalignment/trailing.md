# trailing

**Framework**: SwiftUI  
**Kind**: property

Trailing column alignment.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static var trailing: TableColumnAlignment { get }
```

#### Discussion

With a `layoutDirection` of `leftToRight`, this is equivalent to right; and with a `layoutDirection` of `rightToLeft`, this is equivalent to left.

## See Also

- [static var automatic: TableColumnAlignment](tablecolumnalignment/automatic.md)
  The default column alignment.
- [static var leading: TableColumnAlignment](tablecolumnalignment/leading.md)
  Leading column alignment.
- [static var center: TableColumnAlignment](tablecolumnalignment/center.md)
  Center column alignment.
- [static var numeric: TableColumnAlignment](tablecolumnalignment/numeric.md)
  Column alignment appropriate for numeric content.
- [static func numeric(Locale.NumberingSystem) -> TableColumnAlignment](tablecolumnalignment/numeric(_:).md)
  Column alignment appropriate for numeric content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumnalignment/trailing)*