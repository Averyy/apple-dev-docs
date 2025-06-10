# infinity

**Framework**: Swift  
**Kind**: property

Positive infinity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
static var infinity: Float80 { get }
```

#### Discussion

Infinity compares greater than all finite numbers and equal to other infinite values.

```swift
let x = Double.greatestFiniteMagnitude
let y = x * 2
// y == Double.infinity
// y > x
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/infinity)*