# init(c0:c1:c2:c3:gamma:cutoff:c4:c5:)

**Framework**: Accelerate  
**Kind**: init

Creates a structure that represents a transfer function to convert from linear to nonlinear RGB.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(c0: CGFloat, c1: CGFloat, c2: CGFloat, c3: CGFloat, gamma: CGFloat, cutoff: CGFloat, c4: CGFloat, c5: CGFloat)
```

#### Return Value

A new structure that represents a transfer function.

#### Discussion

Listing 1.

```objc
if (R >= cutoff) {
    R' = c0 * pow( c1 * R + c2, gamma ) + c3
} 
else {
    R' = c4 * R + c5                             
}
```

## Parameters

- `c0`: The   value in the transfer function.
- `c1`: The   value in the transfer function.
- `c2`: The   value in the transfer function.
- `c3`: The   value in the transfer function.
- `gamma`: The   value in the transfer function.
- `cutoff`: The   value in the transfer function.
- `c4`: The   value in the transfer function.
- `c5`: The   value in the transfer function.

## See Also

- [init()](vimagetransferfunction/init.md)
  Creates an empty transfer function structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagetransferfunction/init(c0:c1:c2:c3:gamma:cutoff:c4:c5:))*