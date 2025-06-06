# object

**Framework**: Combine  
**Kind**: property

The object that contains the property to assign.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
final var object: Root? { get }
```

#### Discussion

The subscriber holds a strong reference to this object until the upstream publisher calls [`receive(completion:)`](subscriber/receive(completion:).md), at which point the subscriber sets this property to `nil`.

## See Also

- [let keyPath: ReferenceWritableKeyPath<Root, Input>](subscribers/assign/keypath.md)
  The key path that indicates the property to assign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/assign/object)*