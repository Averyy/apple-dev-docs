# subscript(_:)

**Framework**: Create ML  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses the element at the given row.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript(index: Int) -> Element { get }
```

Available when `Element` conforms to `MLDataValueConvertible`.

**Other overloads**:

```swift
subscript(mask: MLDataColumn<Bool>) -> MLDataColumn<Element> { get }
```

```swift
subscript(mask: MLUntypedColumn) -> MLDataColumn<Element> { get }
```

```swift
subscript(slice: Range<Int>) -> MLDataColumn<Element> { get }
```

```swift
subscript<R>(slice: R) -> MLDataColumn<Element> where R : RangeExpression, R.Bound == Int { get }
```

## Return Value

The `Element` at the given index.

## Parameters

- `index`: A row number of the column, beginning with `0`.

## See Also

### Getting an element
- [func element(at: Int) -> Element?](./element%28at%29.md)
  Accesses the element at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/subscript(_:))*