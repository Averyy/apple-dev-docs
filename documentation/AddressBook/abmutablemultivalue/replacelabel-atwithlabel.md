# replaceLabel(at:withLabel:)

**Framework**: Address Book  
**Kind**: method

Replaces the label at the given index.

**Availability**:
- macOS ?+

## Declaration

```swift
func replaceLabel(at index: Int, withLabel label: String!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if successful; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

If the label is `nil` or if the index is out of bounds, this method raises an exception.

## Parameters

- `index`: The index of the label that will be replaced.
- `label`: The new label.

## See Also

- [func replace(at: Int, withValue: Any!) -> Bool](abmutablemultivalue/replace(at:withvalue:).md)
  Replaces the value at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmutablemultivalue/replacelabel(at:withlabel:))*