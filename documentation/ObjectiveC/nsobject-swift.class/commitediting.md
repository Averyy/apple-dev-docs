# commitEditing

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns whether the receiver was able to commit any pending edits.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

## Declaration

```objc
- (BOOL) commitEditing;
```

#### Return Value

[`YES`](../yes.md) if the changes were successfully applied to the model, [`NO`](../no.md) otherwise.

#### Discussion

A commit is denied if the receiver fails to apply the changes to the model object, perhaps due to a validation error.

## See Also

### Related Documentation
- [- discardEditing](./discardediting.md)
  Causes the receiver to discard any changes, restoring the previous values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/commitediting)*