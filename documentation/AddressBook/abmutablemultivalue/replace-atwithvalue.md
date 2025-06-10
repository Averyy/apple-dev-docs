# replace(at:withValue:)

**Framework**: Address Book  
**Kind**: method

Replaces the value at the given index.

**Availability**:
- macOS ?+

## Declaration

```swift
func replace(at index: Int, withValue value: Any!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if successful; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If the value is `nil` or if the index is out of bounds, this method raises an exception.

## Parameters

- `index`: The index of the value that will be replaced.
- `value`: The new value.

## See Also

- [func replaceLabel(at: Int, withLabel: String!) -> Bool](abmutablemultivalue/replacelabel(at:withlabel:).md)
  Replaces the label at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmutablemultivalue/replace(at:withvalue:))*