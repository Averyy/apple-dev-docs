# toggle()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Toggles the Boolean variable’s value.

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
mutating func toggle()
```

## Discussion

Use this method to toggle a Boolean value from `true` to `false` or from `false` to `true`.

```swift
var bools = [true, false]

bools[0].toggle()
// bools == [false, false]
```

## See Also

### Transforming a Boolean
- [static func ! (Bool) -> Bool](./not%28_%29.md)
  Performs a logical NOT operation on a Boolean value.
- [static func || (Bool, @autoclosure () throws -> Bool) rethrows -> Bool](./opop%28_,_%29.md)
  Performs a logical OR operation on two Boolean values.
- [static func && (Bool, @autoclosure () throws -> Bool) rethrows -> Bool](./ampamp%28_,_%29.md)
  Performs a logical AND operation on two Boolean values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/bool/toggle())*