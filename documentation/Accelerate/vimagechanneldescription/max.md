# max

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The maximum encoded value.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var max: CGFloat
```

```c
CGFloat max;
```

## Discussion

The vImage library clamps values greater than the maximum to the maximum.

## See Also

### Instance properties
- [var min: CGFloat](./min.md)
  The minimum encoded value.
- [var zero: CGFloat](./zero.md)
  The encoding for the value zero.
- [var full: CGFloat](./full.md)
  The encoding for the value one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagechanneldescription/max)*