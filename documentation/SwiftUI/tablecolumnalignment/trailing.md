# trailing

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

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

### Getting the alignment
- [static var automatic: TableColumnAlignment](./automatic.md)
  The default column alignment.
- [static var leading: TableColumnAlignment](./leading.md)
  Leading column alignment.
- [static var center: TableColumnAlignment](./center.md)
  Center column alignment.
- [static var numeric: TableColumnAlignment](./numeric.md)
  Column alignment appropriate for numeric content.
- [static func numeric(Locale.NumberingSystem) -> TableColumnAlignment](./numeric%28_%29.md)
  Column alignment appropriate for numeric content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumnalignment/trailing)*