# removeAndLabel(at:)

**Framework**: Address Book  
**Kind**: method

Removes the value and label at the given index.

**Availability**:
- macOS ?+

## Declaration

```swift
func removeAndLabel(at index: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if successful; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If the index is out of bounds, this method raises an exception.

## Parameters

- `index`: The index of the value-label pair that will be removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmutablemultivalue/removeandlabel(at:))*