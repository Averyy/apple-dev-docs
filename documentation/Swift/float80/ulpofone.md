# ulpOfOne

**Framework**: Swift  
**Kind**: property

The unit in the last place of 1.0.

**Availability**:
- macOS 10.10+

## Declaration

```swift
static var ulpOfOne: Float80 { get }
```

#### Discussion

The positive difference between 1.0 and the next greater representable number. The `ulpOfOne` constant corresponds to the C macros `FLT_EPSILON`, `DBL_EPSILON`, and others with a similar purpose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/ulpofone)*