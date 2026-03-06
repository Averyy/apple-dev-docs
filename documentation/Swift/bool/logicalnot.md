# !(_:)

**Framework**: Swift  
**Kind**: op

Performs a logical NOT operation on a Boolean value.

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
static func ! (a: Bool) -> Bool
```

#### Discussion

The logical NOT operator (`!`) inverts a Boolean value. If the value is `true`, the result of the operation is `false`; if the value is `false`, the result is `true`.

```swift
var printedMessage = false

if !printedMessage {
    print("You look nice today!")
    printedMessage = true
}
// Prints "You look nice today!"
```

## Parameters

- `a`: The Boolean value to negate.

## See Also

- [func toggle()](bool/toggle.md)
  Toggles the Boolean variable’s value.
- [static func || (Bool, @autoclosure () throws -> Bool) rethrows -> Bool](bool/__(_:_:).md)
  Performs a logical OR operation on two Boolean values.
- [static func && (Bool, @autoclosure () throws -> Bool) rethrows -> Bool](bool/&&(_:_:).md)
  Performs a logical AND operation on two Boolean values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/bool/!(_:))*