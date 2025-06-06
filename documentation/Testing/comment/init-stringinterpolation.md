# init(stringInterpolation:)

**Framework**: Swift Testing  
**Kind**: init

Creates a new instance from an interpolated string literal.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
init(stringInterpolation: DefaultStringInterpolation)
```

#### Discussion

Don’t call this initializer directly. It’s used by the compiler when you create a string using string interpolation. Instead, use string interpolation to create a new string by including values, literals, variables, or expressions enclosed in parentheses, prefixed by a backslash (`\(`…`)`).

```None
let price = 2
let number = 3
let message = """
              If one cookie costs \(price) dollars, \
              \(number) cookies cost \(price * number) dollars.
              """
// message == "If one cookie costs 2 dollars, 3 cookies cost 6 dollars."
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/comment/init(stringinterpolation:))*