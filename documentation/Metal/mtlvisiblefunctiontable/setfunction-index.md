# setFunction(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Sets a table entry to point to a callable function.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setFunction(_ function: (any MTLFunctionHandle)?, index: Int)
```

## Parameters

- `function`: A function handle for the function to be called.
- `index`: The index of the table entry to change.

## See Also

- [func setFunctions([(any MTLFunctionHandle)?], range: Range<Int>)](mtlvisiblefunctiontable/setfunctions(_:range:).md)
  Sets a range of table entries to point to an array of callable functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvisiblefunctiontable/setfunction(_:index:))*