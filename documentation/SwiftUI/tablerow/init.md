# init(_:)

**Framework**: SwiftUI  
**Kind**: init

Creates a table row for the given value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
init(_ value: Value)
```

#### Discussion

The table provides the value of a row to each column of a table, which produces the cells for each row in the column.

The following example creates a row for one instance of the `Person` type. The table delivers this value to its columns, which displays different fields of `Person`.

```swift
 TableRow(Person(givenName: "Tom", familyName: "Clark"))
```

## Parameters

- `value`: The value of the row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablerow/init(_:))*