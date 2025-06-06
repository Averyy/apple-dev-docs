# ??(_:_:)

**Framework**: Swift  
**Kind**: op

Performs a nil-coalescing operation, returning the wrapped value of an `Optional` instance or a default `Optional` value.

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
func ?? <T>(optional: consuming T?, defaultValue: @autoclosure () throws -> T?) rethrows -> T? where T : ~Copyable
```

#### Discussion

A nil-coalescing operation unwraps the left-hand side if it has a value, or returns the right-hand side as a default. The result of this operation will be the same type as its arguments.

This operator uses short-circuit evaluation: `optional` is checked first, and `defaultValue` is evaluated only if `optional` is `nil`. For example:

```swift
let goodNumber = Int("100") ?? Int("42")
print(goodNumber)
// Prints "Optional(100)"

let notSoGoodNumber = Int("invalid-input") ?? Int("42")
print(notSoGoodNumber)
// Prints "Optional(42)"
```

In this example, `goodNumber` is assigned a value of `100` because `Int("100")` succeeds in returning a non-`nil` result. When `notSoGoodNumber` is initialized, `Int("invalid-input")` fails and returns `nil`, and so `Int("42")` is called to supply a default value.

Because the result of this nil-coalescing operation is itself an optional value, you can chain default values by using `??` multiple times. The first optional value that isn’t `nil` stops the chain and becomes the result of the whole expression. The next example tries to find the correct text for a greeting in two separate dictionaries before falling back to a static default.

```swift
let greeting = userPrefs[greetingKey] ??
    defaults[greetingKey] ?? "Greetings!"
```

If `userPrefs[greetingKey]` has a value, that value is assigned to `greeting`. If not, any value in `defaults[greetingKey]` will succeed, and if not that, `greeting` will be set to the non-optional default value, `"Greetings!"`.

## Parameters

- `optional`: An optional value.
- `defaultValue`: A value to use as a default.   and    have the same type.

## See Also

- [func ?? <T>(consuming T?, @autoclosure () throws -> T) rethrows -> T](__(_:_:)-9xjze.md)
  Performs a nil-coalescing operation, returning the wrapped value of an `Optional` instance or a default value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/__(_:_:)-1fjjj)*