# !=(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a Boolean value indicating whether two types are not identical.

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
func != (t0: (any Any.Type)?, t1: (any Any.Type)?) -> Bool
```

#### Return Value

`true` if one, but not both, of `t0` and `t1` are `nil`, or if they represent different types; otherwise, `false`.

## Parameters

- `t0`: A type to compare.
- `t1`: Another type to compare.

## See Also

- [struct Mirror](mirror.md)
  A representation of the substructure and display style of an instance of any type.
- [struct ObjectIdentifier](objectidentifier.md)
  A unique identifier for a class instance or metatype.
- [func type<T, Metatype>(of: T) -> Metatype](type(of:).md)
  Returns the dynamic type of a value.
- [func == ((any Any.Type)?, (any Any.Type)?) -> Bool](==(_:_:)-w1qf.md)
  Returns a Boolean value indicating whether two types are identical.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/!=(_:_:)-6s4z0)*