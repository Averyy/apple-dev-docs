# subscript(_:)

**Framework**: Create ML  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses the element at the given position.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript(index: Int) -> MLDataValue { get }
```

**Other overloads**:

```swift
subscript(mask: MLDataColumn<Bool>) -> MLUntypedColumn { get }
```

```swift
subscript(mask: MLUntypedColumn) -> MLUntypedColumn { get }
```

```swift
subscript(slice: Range<Int>) -> MLUntypedColumn { get }
```

```swift
subscript<R>(slice: R) -> MLUntypedColumn where R : RangeExpression, R.Bound == Int { get }
```

#### Return Value

The value at the given index.

## Parameters

- `index`: The index of an element in the column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/subscript(_:)-6j6rb)*