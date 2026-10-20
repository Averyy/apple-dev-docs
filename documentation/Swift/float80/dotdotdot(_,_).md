# ...(_:_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator

Returns a closed range that contains both of its bounds.

**Availability**:
- macOS 10.10+

## Declaration

```swift
static func ... (minimum: Self, maximum: Self) -> ClosedRange<Self>
```

#### Discussion

Use the closed range operator (`...`) to create a closed range of any type that conforms to the `Comparable` protocol. This example creates a `ClosedRange<Character>` from “a” up to, and including, “z”.

```swift
let lowercase = "a"..."z"
print(lowercase.contains("z"))
// Prints "true"
```

> **Precondition**: `minimum <= maximum`.

## Parameters

- `minimum`: The lower bound for the range.
- `maximum`: The upper bound for the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/'...(_:_:))*