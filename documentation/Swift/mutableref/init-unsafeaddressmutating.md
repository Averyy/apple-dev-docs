# init(unsafeAddress:mutating:)

**Framework**: Swift  
**Kind**: init

Unsafely initializes an instance of `MutableRef` using the given ‘unsafeAddress’ as the mutable reference based on the mutating lifetime of the given ‘owner’ argument.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init<Owner>(unsafeAddress pointer: UnsafeMutablePointer<Value>, mutating owner: inout Owner) where Owner : ~Copyable, Owner : ~Escapable
```

## Parameters

- `pointer`: The address to use to mutably reference an instance of type `Value`.
- `owner`: The owning instance that this `MutableRef` instance’s lifetime is based on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutableref/init(unsafeaddress:mutating:))*