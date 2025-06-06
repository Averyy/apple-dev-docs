# map(to:)

**Framework**: Create ML  
**Kind**: method

Creates a new column of typed values by converting this untyped column to the given type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func map<T>(to type: T.Type) -> MLDataColumn<T> where T : MLDataValueConvertible
```

#### Return Value

A new data column if the column’s underlying type is convertible to given type; otherwise `nil`.

#### Discussion

Use this method to convert the elements of the column to a data column of the given type via [`MLDataValueConvertible`](mldatavalueconvertible.md). Unlike [`column(type:)`](mluntypedcolumn/column(type:).md), which doesn’t alter its elements, [`map(to:)`](mluntypedcolumn/map(to:).md) converts the elements to the destination type. For example, you can use [`map(to:)`](mluntypedcolumn/map(to:).md) to convert an untyped column of integers to a data column of strings.

## Parameters

- `type`: A metatype used to create a new data column of that type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/map(to:))*