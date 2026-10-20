# replace(at:withValue:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Replaces the value at the given index.

**Availability**:
- macOS

## Declaration

```swift
func replace(at index: Int, withValue value: Any!) -> Bool
```

```objc
- (BOOL) replaceValueAtIndex:(NSUInteger) index withValue:(id) value;
```

#### Return Value

[`true`](../../Swift/true.md) if successful; otherwise [`false`](../../Swift/false.md).

#### Discussion

If the value is `nil` or if the index is out of bounds, this method raises an exception.

## Parameters

- `index`: The index of the value that will be replaced.
- `value`: The new value.

## See Also

### Replacing values and labels
- [func replaceLabel(at: Int, withLabel: String!) -> Bool](./replacelabel%28at,withlabel%29.md)
  Replaces the label at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmutablemultivalue-swift.class/replace(at:withvalue:))*