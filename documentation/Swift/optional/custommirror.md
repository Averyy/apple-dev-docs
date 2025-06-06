# customMirror

**Framework**: Swift  
**Kind**: property

The custom mirror for this instance.

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
var customMirror: Mirror { get }
```

#### Discussion

If this type has value semantics, the mirror should be unaffected by subsequent mutations of the instance.

## See Also

- [func hash(into: inout Hasher)](optional/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var unsafelyUnwrapped: Wrapped](optional/unsafelyunwrapped.md)
  The wrapped value of this instance, unwrapped without checking whether the instance is `nil`.
- [var debugDescription: String](optional/debugdescription.md)
  A textual representation of this instance, suitable for debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/custommirror)*