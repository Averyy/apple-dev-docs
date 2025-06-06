# prototype

**Framework**: TabularData  
**Kind**: property

A prototype that creates type-erased columns with the same underlying type as the column slice.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var prototype: any AnyColumnPrototype { get }
```

#### Discussion

Use a type-erased column prototype to create new columns of the same type as the slice’s parent column without explicitly knowing what type it is, by calling the `prototype` property’s [`makeColumn(capacity:)`](anycolumnprototype/makecolumn(capacity:).md) method.

```swift
// Get a type-erased column.
let someColumn: AnyColumn = dataFrame["someFeature"]

// Create a new column with the same type.
let newColumn = someColumn.prototype.makeColumn(capacity: 10)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumn/prototype)*