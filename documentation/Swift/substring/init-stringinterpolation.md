# init(stringInterpolation:)

**Framework**: Swift  
**Kind**: init

Creates a new instance from an interpolated string literal.

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
init(stringInterpolation: DefaultStringInterpolation)
```

#### Discussion

Do not call this initializer directly. It is used by the compiler when you create a string using string interpolation. Instead, use string interpolation to create a new string by including values, literals, variables, or expressions enclosed in parentheses, prefixed by a backslash (`\(`…`)`).

```swift
let price = 2
let number = 3
let message = """
              If one cookie costs \(price) dollars, \
              \(number) cookies cost \(price * number) dollars.
              """
print(message)
// Prints "If one cookie costs 2 dollars, 3 cookies cost 6 dollars."
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/init(stringinterpolation:))*