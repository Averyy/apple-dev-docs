# init(unsafeAddress:mutating:)

**Framework**: Swift  
**Kind**: init

Unsafely initializes an instance of `MutableRef` using the given ‘unsafeAddress’ as the mutable reference based on the mutating lifetime of the given ‘owner’ argument.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init<Owner>(unsafeAddress pointer: UnsafeMutablePointer<Value>, mutating owner: inout Owner) where Owner : ~Copyable, Owner : ~Escapable
```

## Parameters

- `owner`: The owning instance that this `MutableRef` instance’s lifetime is based on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutableref/init(unsafeaddress:mutating:))*