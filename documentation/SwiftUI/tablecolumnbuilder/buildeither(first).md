# buildEither(first:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Creates a column result for the first of two column content alternatives.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- visionOS 1.1+

## Declaration

```swift
@export(implementation)
static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F> where RowValue == T.TableRowValue, Sort == T.TableColumnSortComparator, T : TableColumnContent, F : TableColumnContent, T.TableColumnSortComparator == F.TableColumnSortComparator, T.TableRowValue == F.TableRowValue
```

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to `SortComparator`.

**Other overloads**:

```swift
@export(implementation)
static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F> where RowValue == T.TableRowValue, T : TableColumnContent, F : TableColumnContent, T.TableColumnSortComparator == Never, T.TableRowValue == F.TableRowValue, F.TableColumnSortComparator == Never
```

#### Discussion

This method provides support for “if” statements in multi-statement closures, producing conditional content for the “then” branch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumnbuilder/buildeither(first:))*