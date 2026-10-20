# setFunctions(_:range:)

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
- visionOS

## Declaration

```swift
func setFunctions(_ functions: [(any MTLFunctionHandle)?], range: Range<Int>)
```

## Parameters

- `functions`: The new entries for the table.
- `range`: A range of indices to change in the table.

## See Also

### Setting a table entry
- [func setFunction((any MTLFunctionHandle)?, index: Int)](./setfunction%28_,index%29.md)
  Sets an entry in the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setfunctions(_:range:))*