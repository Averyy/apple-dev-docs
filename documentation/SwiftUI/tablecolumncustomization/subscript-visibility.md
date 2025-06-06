# subscript(visibility:)

**Framework**: SwiftUI  
**Kind**: subscript

The visibility of the column identified by its identifier.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
subscript(visibility id: String) -> Visibility { get set }
```

#### Overview

Explicit identifiers can be associated with a `TableColumn` using the `customizationID(_:)` modifier.

```swift
TableColumn("Number of Reports", value: \.duplicateCount) {
    Text($0.duplicateCount, format: .number)
}
.customizationID("numberOfReports")

...

columnsCustomization[visibility: "numberOfReports"] = .hidden
```

If the ID isn’t associated with the state, a default value of `.automatic` is returned.

## See Also

- [func resetOrder()](tablecolumncustomization/resetorder.md)
  Resets the column order back to the default, preserving the customized visibility and size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumncustomization/subscript(visibility:))*