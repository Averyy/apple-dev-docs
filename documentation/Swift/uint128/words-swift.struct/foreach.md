# forEach(_:)

**Framework**: Swift  
**Kind**: method

Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.

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
func forEach(_ body: (Self.Element) throws -> Void) rethrows
```

#### Discussion

The two loops in the following example produce the same output:

```swift
let numberWords = ["one", "two", "three"]
for word in numberWords {
    print(word)
}
// Prints "one"
// Prints "two"
// Prints "three"

numberWords.forEach { word in
    print(word)
}
// Same as above
```

Using the `forEach` method is distinct from a `for`-`in` loop in two important ways:

1. You cannot use a `break` or `continue` statement to exit the current call of the `body` closure or skip subsequent calls.
2. Using the `return` statement in the `body` closure will exit only from the current call to `body`, not from any outer scope, and won’t skip subsequent calls.

## Parameters

- `body`: A closure that takes an element of the sequence as a   parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint128/words-swift.struct/foreach(_:))*