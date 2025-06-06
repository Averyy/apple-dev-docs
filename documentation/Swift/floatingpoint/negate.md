# negate()

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Replaces this value with its additive inverse.

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
override mutating func negate()
```

#### Discussion

The result is always exact. This example uses the `negate()` method to negate the value of the variable `x`:

```swift
var x = 21.5
x.negate()
// x == -21.5
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/floatingpoint/negate())*