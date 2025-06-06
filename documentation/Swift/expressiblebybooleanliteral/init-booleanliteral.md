# init(booleanLiteral:)

**Framework**: Swift  
**Kind**: init  
**Required**: Yes

Creates an instance initialized to the given Boolean value.

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
init(booleanLiteral value: Self.BooleanLiteralType)
```

#### Discussion

Do not call this initializer directly. Instead, initialize a variable or constant using one of the Boolean literals `true` and `false`. For example:

```swift
let twasBrillig = true
```

In this example, the assignment to the `twasBrillig` constant calls this Boolean literal initializer behind the scenes.

## Parameters

- `value`: The value of the new instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/expressiblebybooleanliteral/init(booleanliteral:))*