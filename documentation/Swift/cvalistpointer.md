# CVaListPointer

**Framework**: Swift  
**Kind**: struct

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
@frozen
struct CVaListPointer
```

## Mentions

- [Using Imported C Functions in Swift](using-imported-c-functions-in-swift.md)

## Topics

### Default Implementations
- [CustomDebugStringConvertible Implementations](cvalistpointer/customdebugstringconvertible-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)

## See Also

- [func withVaList<R>([any CVarArg], (CVaListPointer) -> R) -> R](withvalist(_:_:).md)
  Invokes the given closure with a C `va_list` argument derived from the given array of arguments.
- [protocol CVarArg](cvararg.md)
  A type whose instances can be encoded, and appropriately passed, as elements of a C `va_list`.
- [func getVaList([any CVarArg]) -> CVaListPointer](getvalist(_:).md)
  Returns a `CVaListPointer` that is backed by autoreleased storage, built from the given array of arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/cvalistpointer)*