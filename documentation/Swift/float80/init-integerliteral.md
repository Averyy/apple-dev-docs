# init(integerLiteral:)

**Framework**: Swift  
**Kind**: init

Creates an instance initialized to the specified integer value.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init(integerLiteral value: Int64)
```

#### Discussion

Do not call this initializer directly. Instead, initialize a variable or constant using an integer literal. For example:

```swift
let x = 23
```

In this example, the assignment to the `x` constant calls this integer literal initializer behind the scenes.

## Parameters

- `value`: The value to create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/init(integerliteral:))*