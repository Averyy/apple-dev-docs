# init(floatLiteral:)

**Framework**: Swift  
**Kind**: init

Creates an instance initialized to the specified floating-point value.

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
init(floatLiteral value: Float16)
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float16/init(floatliteral:))*