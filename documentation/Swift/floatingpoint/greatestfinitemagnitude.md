# greatestFiniteMagnitude

**Framework**: Swift  
**Kind**: property  
**Required**: Yes

The greatest finite number representable by this type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var greatestFiniteMagnitude: Self { get }
```

#### Discussion

This value compares greater than or equal to all finite numbers, but less than `infinity`.

This value corresponds to type-specific C macros such as `FLT_MAX` and `DBL_MAX`. The naming of those macros is slightly misleading, because `infinity` is greater than this value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/floatingpoint/greatestfinitemagnitude)*