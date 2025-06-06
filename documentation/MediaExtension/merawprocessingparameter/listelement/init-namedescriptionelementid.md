# init(name:description:elementID:)

**Framework**: MediaExtension  
**Kind**: init

Creates a list element parameter object with the element id value.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init(name: String, description: String, elementID: Int)
```

#### Return Value

An instance of [`MERAWProcessingParameter.ListElement`](merawprocessingparameter/listelement.md).

## Parameters

- `name`: A localized human-readable name for the parameter, suitable for displaying in application UI.
- `description`: A localized description of the parameter, suitable for displaying in a tool tip or similar explanatory UI.
- `elementID`: A unique number in the list which represents this list option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/listelement/init(name:description:elementid:))*