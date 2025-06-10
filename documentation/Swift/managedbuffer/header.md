# header

**Framework**: Swift  
**Kind**: property

The stored `Header` instance.

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
final var header: Header
```

#### Discussion

During instance creation, in particular during `ManagedBuffer.create`’s call to initialize, `ManagedBuffer`’s `header` property is as-yet uninitialized, and therefore reading the `header` property during `ManagedBuffer.create` is undefined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/managedbuffer/header)*