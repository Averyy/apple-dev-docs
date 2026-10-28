# NSStringFromUIEdgeInsets

**Framework**: UIKit  
**Kind**: func  
**Role**: Function

Returns a string formatted to contain the data from an edge insets structure.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 2.0+

## Declaration

```c
extern NSString *NSStringFromUIEdgeInsets(UIEdgeInsets insets);
```

## Return Value

A string that corresponds to `insets`. See [`UIEdgeInsetsFromString`](./uiedgeinsetsfromstring.md) for a discussion of the string format.

## Parameters

- `insets`: A UIKit edge insets data structure.

## See Also

### Converting to and from strings
- [UIEdgeInsetsFromString](./uiedgeinsetsfromstring.md)
  Returns a UIKit edge insets structure based on the data in the specified string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsstringfromuiedgeinsets)*