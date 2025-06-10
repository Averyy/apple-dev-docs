# pi

**Framework**: Swift  
**Kind**: property

The mathematical constant pi (π), approximately equal to 3.14159.

**Availability**:
- macOS 10.10+

## Declaration

```swift
static var pi: Float80 { get }
```

#### Discussion

When measuring an angle in radians, π is equivalent to a half-turn.

This value is rounded toward zero to keep user computations with angles from inadvertently ending up in the wrong quadrant. A type that conforms to the `FloatingPoint` protocol provides the value for `pi` at its best possible precision.

```swift
print(Double.pi)
// Prints "3.14159265358979"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/pi)*