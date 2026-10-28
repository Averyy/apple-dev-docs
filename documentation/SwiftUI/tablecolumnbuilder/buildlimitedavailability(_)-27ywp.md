# buildLimitedAvailability(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+
- visionOS 1.2+

## Declaration

```swift
@export(implementation)
static func buildLimitedAvailability(_ content: any TableColumnContent<RowValue, Sort>) -> some TableColumnContent<RowValue, Sort>
```

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to `SortComparator`.

**Other overloads**:

```swift
@export(implementation)
static func buildLimitedAvailability(_ content: any TableColumnContent<RowValue, Never>) -> some TableColumnContent<RowValue, Never>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumnbuilder/buildlimitedavailability(_:)-27ywp)*