# AtomicOptionalRepresentation

**Framework**: Synchronization  
**Kind**: associatedtype  
**Required**: Yes

The storage representation type that encodes to and decodes from `Optional<Self>` which is a suitable type when used in atomic operations on `Optional`.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
associatedtype AtomicOptionalRepresentation : BitwiseCopyable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomicoptionalrepresentable/atomicoptionalrepresentation)*