# +(_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator

Returns the given number unchanged.

**Availability**:
- macOS 10.10+

## Declaration

```swift
static func + (x: Self) -> Self
```

#### Return Value

The given argument without any changes.

#### Discussion

You can use the unary plus operator (`+`) to provide symmetry in your code for positive numbers when also using the unary minus operator.

```swift
let x = -21
let y = +21
// x == -21
// y == 21
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/+(_:))*