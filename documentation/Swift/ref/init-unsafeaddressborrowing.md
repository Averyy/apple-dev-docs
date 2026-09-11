# init(unsafeAddress:borrowing:)

**Framework**: Swift  
**Kind**: init

Unsafely initializes an instance of `Ref` using the given ‘unsafeAddress’ as the reference based on the borrowed lifetime of the given ‘owner’ argument.

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
init<Owner>(unsafeAddress pointer: UnsafePointer<Value>, borrowing owner: borrowing Owner) where Owner : ~Copyable, Owner : ~Escapable
```

## Parameters

- `pointer`: The address to use to reference an instance of type `Value`.
- `owner`: The owning instance that this `Ref` instance’s lifetime is based on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/ref/init(unsafeaddress:borrowing:))*