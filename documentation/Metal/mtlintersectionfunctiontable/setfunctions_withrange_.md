# setFunctions:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Sets a range of entries in the table.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setFunctions:(id<MTLFunctionHandle> const[]) functions withRange:(NSRange) range;
```

## Parameters

- `functions`: A pointer to an array of function handles.
- `range`: A range of indices to change in the table.

## See Also

### Setting a table entry
- [func setFunction((any MTLFunctionHandle)?, index: Int)](./setfunction%28_,index%29.md)
  Sets an entry in the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setfunctions:withrange:)*