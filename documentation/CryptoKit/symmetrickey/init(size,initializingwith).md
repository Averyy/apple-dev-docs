# init(size:initializingWith:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a new key of the given size where the key contents are initialized via a callback.

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
init<E>(size: SymmetricKeySize, initializingWith callback: @_lifetime(0: copy 0) (inout OutputRawSpan) throws(E) -> Void) throws(E) where E : Error
```

## Parameters

- `size`: The size of the key to generate. You can use one of the standard sizes, like [`bits256`](symmetrickeysize/bits256.md), or you can create a key of custom length by initializing a [`SymmetricKeySize`](symmetrickeysize.md) instance with a non-standard value.
- `callback`: A callback that will be invoked to initialize the contents of the key. It must initialize the full set of size.bitCount / 8 bytes in the provided output span.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/symmetrickey/init(size:initializingwith:))*