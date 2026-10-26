# NSStringFromDirectionalEdgeInsets

**Framework**: UIKit  
**Kind**: func  
**Role**: Function

Returns a string formatted to contain the data from a directional edge insets structure.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```c
extern NSString *NSStringFromDirectionalEdgeInsets(NSDirectionalEdgeInsets insets);
```

#### Return Value

A string that corresponds to insets. See [`NSDirectionalEdgeInsetsFromString`](./nsdirectionaledgeinsetsfromstring.md) for a discussion of the string format.

## Parameters

- `insets`: A directional edge insets data structure.

## See Also

### Converting to and from strings
- [NSDirectionalEdgeInsetsFromString](./nsdirectionaledgeinsetsfromstring.md)
  Returns a directional edge insets structure based on data in the specified string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsstringfromdirectionaledgeinsets)*