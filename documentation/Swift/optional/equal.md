# ==(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a Boolean value indicating whether two optional instances are equal.

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
static func == (lhs: Wrapped?, rhs: Wrapped?) -> Bool
```

#### Discussion

Use this equal-to operator (`==`) to compare any two optional instances of a type that conforms to the `Equatable` protocol. The comparison returns `true` if both arguments are `nil` or if the two arguments wrap values that are equal. Conversely, the comparison returns `false` if only one of the arguments is `nil` or if the two arguments wrap values that are not equal.

```swift
let group1 = [1, 2, 3, 4, 5]
let group2 = [1, 3, 5, 7, 9]
if group1.first == group2.first {
    print("The two groups start the same.")
}
// Prints "The two groups start the same."
```

You can also use this operator to compare a non-optional value to an optional that wraps the same type. The non-optional value is wrapped as an optional before the comparison is made. In the following example, the `numberToMatch` constant is wrapped as an optional before comparing to the optional `numberFromString`:

```swift
let numberToMatch: Int = 23
let numberFromString: Int? = Int("23")      // Optional(23)
if numberToMatch == numberFromString {
    print("It's a match!")
}
// Prints "It's a match!"
```

An instance that is expressed as a literal can also be used with this operator. In the next example, an integer literal is compared with the optional integer `numberFromString`. The literal `23` is inferred as an `Int` instance and then wrapped as an optional before the comparison is performed.

```swift
if 23 == numberFromString {
    print("It's a match!")
}
// Prints "It's a match!"
```

## Parameters

- `lhs`: An optional value to compare.
- `rhs`: Another optional value to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/==(_:_:)-m6x)*