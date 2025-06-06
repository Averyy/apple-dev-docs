# init(booleanLiteral:)

**Framework**: Swift  
**Kind**: init

Creates an instance initialized to the specified Boolean literal.

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
init(booleanLiteral value: Bool)
```

#### Discussion

Do not call this initializer directly. It is used by the compiler when you use a Boolean literal. Instead, create a new `Bool` instance by using one of the Boolean literals `true` or `false`.

```swift
var printedMessage = false

if !printedMessage {
    print("You look nice today!")
    printedMessage = true
}
// Prints "You look nice today!"
```

In this example, both assignments to the `printedMessage` variable call this Boolean literal initializer behind the scenes.

## Parameters

- `value`: The value of the new instance.

## See Also

- [init()](bool/init.md)
  Creates an instance initialized to `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/bool/init(booleanliteral:))*