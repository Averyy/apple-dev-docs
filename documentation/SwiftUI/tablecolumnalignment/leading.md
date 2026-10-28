# leading

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

Leading column alignment.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static var leading: TableColumnAlignment { get }
```

## Discussion

With a `layoutDirection` of `leftToRight`, this is equivalent to left; and with a `layoutDirection` of `rightToLeft`, this is equivalent to right.

## See Also

### Getting the alignment
- [static var automatic: TableColumnAlignment](./automatic.md)
  The default column alignment.
- [static var center: TableColumnAlignment](./center.md)
  Center column alignment.
- [static var trailing: TableColumnAlignment](./trailing.md)
  Trailing column alignment.
- [static var numeric: TableColumnAlignment](./numeric.md)
  Column alignment appropriate for numeric content.
- [static func numeric(Locale.NumberingSystem) -> TableColumnAlignment](./numeric%28_%29.md)
  Column alignment appropriate for numeric content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumnalignment/leading)*