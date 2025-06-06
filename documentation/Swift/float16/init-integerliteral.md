# init(integerLiteral:)

**Framework**: Swift  
**Kind**: init

Creates an instance initialized to the specified integer value.

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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float16/init(integerliteral:))*