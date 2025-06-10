# greatestFiniteMagnitude

**Framework**: Swift  
**Kind**: property

The greatest finite number representable by this type.

**Availability**:
- macOS 10.10+

## Declaration

```swift
static var greatestFiniteMagnitude: Float80 { get }
```

#### Discussion

This value compares greater than or equal to all finite numbers, but less than `infinity`.

This value corresponds to type-specific C macros such as `FLT_MAX` and `DBL_MAX`. The naming of those macros is slightly misleading, because `infinity` is greater than this value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/greatestfinitemagnitude)*