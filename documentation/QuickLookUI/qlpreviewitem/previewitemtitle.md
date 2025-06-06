# previewItemTitle

**Framework**: Quick Look UI  
**Kind**: property

The title to display for the preview item.

**Availability**:
- macOS 10.6+

## Declaration

```swift
optional var previewItemTitle: String! { get }
```

#### Discussion

If you don’t implement a getter method for this property, or if your method returns `nil`, Quick Look examines the URL or content of the previewed item to determine an appropriate title. Return a `non-nil` value for this property to provide a custom title.

## See Also

- [var previewItemDisplayState: Any!](qlpreviewitem/previewitemdisplaystate.md)
  The display state for the preview item.
- [var previewItemURL: URL!](qlpreviewitem/previewitemurl.md)
  The URL of the item to preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewitem/previewitemtitle)*