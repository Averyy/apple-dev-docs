# setFunction(_:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) setFunction:(id<MTLFunctionHandle>) function atIndex:(NSUInteger) index;
```

## Parameters

- `function`: A function handle for the function to be called.
- `index`: The index of the table entry to change.

## See Also

### Setting a table entry
- [func setFunctions([(any MTLFunctionHandle)?], range: Range<Int>)](./setfunctions%28_,range%29.md)
  Sets a range of table entries to point to an array of callable functions.
- [- setFunctions:withRange:](./setfunctions_withrange_.md)
  Sets a range of table entries to point to an array of callable functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvisiblefunctiontable/setfunction(_:index:))*