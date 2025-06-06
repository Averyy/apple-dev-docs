# setFunction(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Sets an entry in the table.

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

- `function`: A function handle for the intersection function.
- `index`: The index of the table entry to change.

## See Also

- [func setFunctions([(any MTLFunctionHandle)?], range: Range<Int>)](mtlintersectionfunctiontable/setfunctions(_:range:).md)
  Sets a range of entries in the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setfunction(_:index:))*