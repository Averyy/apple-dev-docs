# negate()

**Framework**: Swift  
**Kind**: method

Replaces this value with its additive inverse.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
mutating func negate()
```

#### Discussion

The result is always exact. This example uses the `negate()` method to negate the value of the variable `x`:

```swift
var x = 21.5
x.negate()
// x == -21.5
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float16/negate())*