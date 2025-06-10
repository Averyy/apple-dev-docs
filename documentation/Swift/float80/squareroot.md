# squareRoot()

**Framework**: Swift  
**Kind**: method

Returns the square root of the value, rounded to a representable value.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func squareRoot() -> Self
```

#### Return Value

The square root of the value.

#### Discussion

The following example declares a function that calculates the length of the hypotenuse of a right triangle given its two perpendicular sides.

```swift
func hypotenuse(_ a: Double, _ b: Double) -> Double {
    return (a * a + b * b).squareRoot()
}

let (dx, dy) = (3.0, 4.0)
let distance = hypotenuse(dx, dy)
// distance == 5.0
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/squareroot())*