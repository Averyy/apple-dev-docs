# materialize()

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Creates a new column by immediately evaluating any lazily applied data processing operations stored in the column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func materialize() throws -> MLDataColumn<Element>
```

Available when `Element` conforms to `MLDataValueConvertible`.

#### Return Value

A new column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/materialize())*