# arcadeButton(row:column:)

**Framework**: Game Controller  
**Kind**: method

Returns the name of the arcade stick button at the specified location.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
static func arcadeButton(row: Int, column: Int) -> GCButtonElementName
```

#### Return Value

The name of an arcade stick button.

## Parameters

- `row`: The row on the arcade stick that the button appears in, where   is the bottom row.
- `column`: The column on the arcade stick that the button appears in, where   is the column nearest to the lever or direction buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcbuttonelementname-swift.struct/arcadebutton(row:column:))*