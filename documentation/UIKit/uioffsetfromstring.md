# UIOffsetFromString

**Framework**: UIKit  
**Kind**: func  
**Role**: Function

Returns a UIKit offset structure corresponding to the data in a given string.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 2.0+

## Declaration

```c
extern UIOffset UIOffsetFromString(NSString *string);
```

## Return Value

An edge insets data structure. If the string is not well-formed, the function returns [`zero`](./uioffset/zero.md).

## Discussion

In general, you should use this function only to convert strings that were previously created using the [`NSStringFromUIOffset`](./nsstringfromuioffset.md) function.

## Parameters

- `string`: A string containing a representation of an offset.

## See Also

### Converting to and from strings
- [NSStringFromUIOffset](./nsstringfromuioffset.md)
  Returns a string formatted to contain the data from an offset structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uioffsetfromstring)*