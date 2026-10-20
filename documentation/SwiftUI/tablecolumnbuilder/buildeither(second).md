# buildEither(second:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Creates a row result for the second of two row content alternatives.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- visionOS 1.1+

## Declaration

```swift
@export(implementation)
static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F> where RowValue == T.TableRowValue, Sort == T.TableColumnSortComparator, T : TableColumnContent, F : TableColumnContent, T.TableColumnSortComparator == F.TableColumnSortComparator, T.TableRowValue == F.TableRowValue
```

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to `SortComparator`.

**Other overloads**:

```swift
@export(implementation)
static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F> where RowValue == T.TableRowValue, T : TableColumnContent, F : TableColumnContent, T.TableColumnSortComparator == Never, T.TableRowValue == F.TableRowValue, F.TableColumnSortComparator == Never
```

#### Discussion

This method provides support for “if” statements in multi-statement closures, producing conditional content for the “else” branch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumnbuilder/buildeither(second:))*