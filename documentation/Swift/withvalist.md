# withVaList(_:_:)

**Framework**: Swift  
**Kind**: func

Invokes the given closure with a C `va_list` argument derived from the given array of arguments.

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
func withVaList<R>(_ args: [any CVarArg], _ body: (CVaListPointer) -> R) -> R
```

## Mentions

- [Using Imported C Functions in Swift](using-imported-c-functions-in-swift.md)

#### Return Value

The return value, if any, of the `body` closure parameter.

#### Discussion

The pointer passed as an argument to `body` is valid only during the execution of `withVaList(_:_:)`. Do not store or return the pointer for later use.

If you need to pass an optional pointer as a `CVarArg` argument, use the `Int(bitPattern:)` initializer to interpret the optional pointer as an `Int` value, which has the same C variadic calling conventions as a pointer on all supported platforms.

## Parameters

- `args`: An array of arguments to convert to a C   pointer.
- `body`: A closure with a   parameter that references the   arguments passed as  . If   has a return value, that value   is also used as the return value for the   function.   The pointer argument is valid only for the duration of the function’s   execution.

## See Also

- [struct CVaListPointer](cvalistpointer.md)
- [protocol CVarArg](cvararg.md)
  A type whose instances can be encoded, and appropriately passed, as elements of a C `va_list`.
- [func getVaList([any CVarArg]) -> CVaListPointer](getvalist(_:).md)
  Returns a `CVaListPointer` that is backed by autoreleased storage, built from the given array of arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withvalist(_:_:))*