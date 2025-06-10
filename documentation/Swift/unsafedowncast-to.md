# unsafeDowncast(_:to:)

**Framework**: Swift  
**Kind**: func

Returns the given instance cast unconditionally to the specified type.

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
func unsafeDowncast<T>(_ x: AnyObject, to type: T.Type) -> T where T : AnyObject
```

#### Return Value

The instance `x`, cast to type `T`.

#### Discussion

The instance passed as `x` must be an instance of type `T`.

Use this function instead of `unsafeBitcast(_:to:)` because this function is more restrictive and still performs a check in debug builds. In -O builds, no test is performed to ensure that `x` actually has the dynamic type `T`.

> ⚠️ **Warning**: This function trades safety for performance. Use `unsafeDowncast(_:to:)` only when you are confident that `x is T` always evaluates to `true`, and only after `x as! T` has proven to be a performance problem.

## Parameters

- `x`: An instance to cast to type  .
- `type`: The type   to which   is cast.

## See Also

- [func unsafeBitCast<T, U>(T, to: U.Type) -> U](unsafebitcast(_:to:).md)
  Returns the bits of the given instance, interpreted as having the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafedowncast(_:to:))*