# removeAndLabel(at:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Removes the value and label at the given index.

**Availability**:
- macOS

## Declaration

```swift
func removeAndLabel(at index: Int) -> Bool
```

```objc
- (BOOL) removeValueAndLabelAtIndex:(NSUInteger) index;
```

#### Return Value

[`true`](../../Swift/true.md) if successful; otherwise [`false`](../../Swift/false.md).

#### Discussion

If the index is out of bounds, this method raises an exception.

## Parameters

- `index`: The index of the value-label pair that will be removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmutablemultivalue-swift.class/removeandlabel(at:))*