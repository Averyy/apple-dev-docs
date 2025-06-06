# assumingType(_:)

**Framework**: TabularData  
**Kind**: method

Returns the underlying typed column.

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
func assumingType<T>(_ type: T.Type) -> Column<T>
```

#### Return Value

A typed column.

#### Discussion

When using this method, you must provide the correct underlying type.

## Parameters

- `type`: The type of the underlying column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumn/assumingtype(_:))*