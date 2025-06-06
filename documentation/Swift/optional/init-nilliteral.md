# init(nilLiteral:)

**Framework**: Swift  
**Kind**: init

Creates an instance initialized with `nil`.

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
init(nilLiteral: ())
```

#### Discussion

Do not call this initializer directly. It is used by the compiler when you initialize an `Optional` instance with a `nil` literal. For example:

```swift
var i: Index? = nil
```

In this example, the assignment to the `i` variable calls this initializer behind the scenes.

## See Also

- [Optional.none](optional/none.md)
  The absence of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/init(nilliteral:))*