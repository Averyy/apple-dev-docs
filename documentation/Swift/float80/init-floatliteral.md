# init(floatLiteral:)

**Framework**: Swift  
**Kind**: init

Creates an instance initialized to the specified floating-point value.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init(floatLiteral value: Float80)
```

#### Discussion

Do not call this initializer directly. Instead, initialize a variable or constant using a floating-point literal. For example:

```swift
let x = 21.5
```

In this example, the assignment to the `x` constant calls this floating-point literal initializer behind the scenes.

## Parameters

- `value`: The value to create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/init(floatliteral:))*