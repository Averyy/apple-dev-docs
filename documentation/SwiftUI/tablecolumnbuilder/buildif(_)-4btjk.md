# buildIf(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Creates a column result for conditional statements.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- visionOS 1.1+

## Declaration

```swift
@export(implementation)
static func buildIf<C>(_ content: C?) -> C? where RowValue == C.TableRowValue, Sort == C.TableColumnSortComparator, C : TableColumnContent
```

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to `SortComparator`.

**Other overloads**:

```swift
@export(implementation)
static func buildIf<C>(_ content: C?) -> C? where RowValue == C.TableRowValue, C : TableColumnContent, C.TableColumnSortComparator == Never
```

## Discussion

This method provides support for “if” statements in multi-statement closures, producing an optional value that is visible only when the condition evaluates to `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumnbuilder/buildif(_:)-4btjk)*