# init(text:cardElements:allowsMultipleLines:)

**Framework**: CarPlay  
**Kind**: init

Initialize a list image row item with a text string, an array of @c CPListImageRowItemCardElement and a boolean to allow multiple lines in this row.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
init(text: String?, cardElements elements: [CPListImageRowItemCardElement], allowsMultipleLines: Bool)
```

#### Discussion

If a nil @c text property is provided the cell will resize accordingly to hide the title.

## Parameters

- `text`: The text visible at the top of the cell.
- `elements`: The list of @c CPListImageRowItemCardElement  elements visible below the text.
- `allowsMultipleLines`: Determines if the elements could be visible on more than a single line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/init(text:cardelements:allowsmultiplelines:))*