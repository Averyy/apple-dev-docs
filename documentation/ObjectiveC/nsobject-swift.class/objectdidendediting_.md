# objectDidEndEditing:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

This message should be sent to the receiver when `editor` has finished editing a property belonging to the receiver.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

## Declaration

```objc
- (void) objectDidEndEditing:(id<NSEditor>) editor;
```

## See Also

### Related Documentation
- [- objectDidBeginEditing:](./objectdidbeginediting_.md)
  This message should be sent to the receiver when `editor` has uncommitted changes that can affect the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/objectdidendediting:)*