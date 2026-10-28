# subscript(_:)

**Framework**: Create ML  
**Kind**: subscript  
**Role**: Instance Subscript

Creates a subset of the table given a range expression of rows.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript<R>(slice: R) -> MLDataTable where R : RangeExpression, R.Bound == Int { get }
```

**Other overloads**:

```swift
subscript(columnName: String) -> MLUntypedColumn { get set }
```

```swift
subscript(mask: MLDataColumn<Bool>) -> MLDataTable { get }
```

```swift
subscript(mask: MLUntypedColumn) -> MLDataTable { get }
```

```swift
subscript(slice: Range<Int>) -> MLDataTable { get }
```

```swift
subscript<Element>(columnName: String) -> MLDataColumn<Element> where Element : MLDataValueConvertible { get set }
```

```swift
subscript<S>(columnNames: S) -> MLDataTable where S : Sequence, S.Element == String { get }
```

## Return Value

A new data table.

## Parameters

- `slice`: An interger range expression indicating which rows to include in the new data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/subscript(_:)-5le8a)*