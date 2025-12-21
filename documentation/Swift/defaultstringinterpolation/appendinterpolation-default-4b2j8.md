# appendInterpolation(_:default:)

**Framework**: Swift  
**Kind**: method

Interpolates the given optional value’s textual representation, or the specified default string, into the string literal being created.

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
mutating func appendInterpolation<T>(_ value: T?, default: @autoclosure () -> some StringProtocol)
```

#### Discussion

You don’t need to call this method directly. It’s used by the compiler when interpreting string interpolations where you provide a `default` parameter. For example, the following code implicitly calls this method, using the value of the `default` parameter when `value` is `nil`:

```swift
var age: Int? = 48
print("Your age is \(age, default: "unknown")")
// Prints: Your age is 48
age = nil
print("Your age is \(age, default: "unknown")")
// Prints: Your age is unknown
```

## Parameters

- `value`: The value to include in a string interpolation, if non- .
- `default`: The string to include if   is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/defaultstringinterpolation/appendinterpolation(_:default:)-4b2j8)*