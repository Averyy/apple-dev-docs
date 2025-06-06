# init(integerLiteral:)

**Framework**: Swift  
**Kind**: init  
**Required**: Yes

Creates an instance initialized to the specified integer value.

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
init(integerLiteral value: Self.IntegerLiteralType)
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/expressiblebyintegerliteral/init(integerliteral:))*