# UIEdgeInsetsFromString

**Framework**: UIKit  
**Kind**: func  
**Role**: Function

Returns a UIKit edge insets structure based on the data in the specified string.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 2.0+

## Declaration

```c
extern UIEdgeInsets UIEdgeInsetsFromString(NSString *string);
```

## Return Value

An edge insets data structure. If the string is not well-formed, the function returns [`zero`](./uiedgeinsets/zero.md).

## Discussion

In general, you should use this function only to convert strings that were previously created using the [`NSStringFromUIEdgeInsets`](./nsstringfromuiedgeinsets.md) function.

## Parameters

- `string`: A string whose contents are of the form “{*top*, *left*, *bottom*, *right*}”, where *top*, *left*, *bottom*, *right* are the floating-point component values of the [`UIEdgeInsets`](./uiedgeinsets.md) structure. An example of a valid string is @”{3.0,8.0,3.0,5.0}”. The string is not localized, so items are always separated with a comma.

## See Also

### Converting to and from strings
- [NSStringFromUIEdgeInsets](./nsstringfromuiedgeinsets.md)
  Returns a string formatted to contain the data from an edge insets structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiedgeinsetsfromstring)*