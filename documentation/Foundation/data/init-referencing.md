# init(referencing:)

**Framework**: Foundation  
**Kind**: init

Initialize a `Data` by adopting a reference type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(referencing reference: NSData)
```

#### Discussion

You can use this initializer to create a `struct Data` that wraps a `class NSData`. `struct Data` will use the `class NSData` for all operations. Other initializers (including casting using `as Data`) may choose to hold a reference or not, based on a what is the most efficient representation.

If the resulting value is mutated, then `Data` will invoke the `mutableCopy()` function on the reference to copy the contents. You may customize the behavior of that function if you wish to return a specialized mutable subclass.

## Parameters

- `reference`: The instance of   that you wish to wrap. This instance will be copied by  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/init(referencing:))*