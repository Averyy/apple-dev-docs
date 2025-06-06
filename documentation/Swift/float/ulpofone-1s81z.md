# ulpOfOne

**Framework**: Swift  
**Kind**: property

The unit in the last place of 1.0.

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
static var ulpOfOne: Self { get }
```

#### Discussion

The positive difference between 1.0 and the next greater representable number. `ulpOfOne` corresponds to the value represented by the C macros `FLT_EPSILON`, `DBL_EPSILON`, etc, and is sometimes called  or . Swift deliberately avoids using the term “epsilon” because:

- Historically “epsilon” has been used to refer to several different concepts in different languages, leading to confusion and bugs.
- The name “epsilon” suggests that this quantity is a good tolerance to choose for approximate comparisons, but it is almost always unsuitable for that purpose.

See also the `ulp` member property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/ulpofone-1s81z)*