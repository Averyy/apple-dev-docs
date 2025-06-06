# getVaList(_:)

**Framework**: Swift  
**Kind**: func

Returns a `CVaListPointer` that is backed by autoreleased storage, built from the given array of arguments.

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
func getVaList(_ args: [any CVarArg]) -> CVaListPointer
```

## Mentions

- [Using Imported C Functions in Swift](using-imported-c-functions-in-swift.md)

#### Return Value

A pointer that can be used with C functions that take a `va_list` argument.

#### Discussion

You should prefer `withVaList(_:_:)` instead of this function. In some uses, such as in a `class` initializer, you may find that the language rules do not allow you to use `withVaList(_:_:)` as intended.

If you need to pass an optional pointer as a `CVarArg` argument, use the `Int(bitPattern:)` initializer to interpret the optional pointer as an `Int` value, which has the same C variadic calling conventions as a pointer on all supported platforms.

## Parameters

- `args`: An array of arguments to convert to a C    pointer.

## See Also

- [func withVaList<R>([any CVarArg], (CVaListPointer) -> R) -> R](withvalist(_:_:).md)
  Invokes the given closure with a C `va_list` argument derived from the given array of arguments.
- [struct CVaListPointer](cvalistpointer.md)
- [protocol CVarArg](cvararg.md)
  A type whose instances can be encoded, and appropriately passed, as elements of a C `va_list`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/getvalist(_:))*