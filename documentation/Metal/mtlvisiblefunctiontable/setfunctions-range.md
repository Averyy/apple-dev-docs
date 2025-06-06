# setFunctions(_:range:)

**Framework**: Metal  
**Kind**: method

Sets a range of table entries to point to an array of callable functions.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
func setFunctions(_ functions: [(any MTLFunctionHandle)?], range: Range<Int>)
```

## Parameters

- `functions`: An array of function handles for the functions to be called.
- `range`: A range of indices to change in the table.

## See Also

- [func setFunction((any MTLFunctionHandle)?, index: Int)](mtlvisiblefunctiontable/setfunction(_:index:).md)
  Sets a table entry to point to a callable function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvisiblefunctiontable/setfunctions(_:range:))*