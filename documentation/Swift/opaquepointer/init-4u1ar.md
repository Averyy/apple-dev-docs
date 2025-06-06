# init(_:)

**Framework**: Swift  
**Kind**: init

Converts a typed `UnsafePointer` to an opaque C pointer.

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
init<T>(_ from: UnsafePointer<T>) where T : ~Copyable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/opaquepointer/init(_:)-4u1ar)*