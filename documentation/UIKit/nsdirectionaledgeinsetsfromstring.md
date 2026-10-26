# NSDirectionalEdgeInsetsFromString

**Framework**: UIKit  
**Kind**: func  
**Role**: Function

Returns a directional edge insets structure based on data in the specified string.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```c
extern NSDirectionalEdgeInsets NSDirectionalEdgeInsetsFromString(NSString *string);
```

#### Return Value

A directional edge insets data structure. If the string is not well-formed, the function returns [`zero`](./nsdirectionaledgeinsets/zero.md).

## Parameters

- `string`: A string whose contents are of the form “{top, leading, bottom, trailing}”, where top, leading, bottom, trailing are the floating-point component values of the [`NSDirectionalEdgeInsets`](./nsdirectionaledgeinsets.md) structure. An example of a valid string is “`{3.0,8.0,3.0,5.0}`”. The string is not localized, so items are always separated with a comma.

## See Also

### Converting to and from strings
- [NSStringFromDirectionalEdgeInsets](./nsstringfromdirectionaledgeinsets.md)
  Returns a string formatted to contain the data from a directional edge insets structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdirectionaledgeinsetsfromstring)*