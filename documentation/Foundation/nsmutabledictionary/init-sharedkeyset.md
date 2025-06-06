# init(sharedKeySet:)

**Framework**: Foundation  
**Kind**: init

Creates a mutable dictionary which is optimized for dealing with a known set of keys.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(sharedKeySet keyset: Any)
```

#### Return Value

A new mutable dictionary optimized for a known set of keys.

#### Discussion

Keys that are not in the key set can still be set in the dictionary, but that usage is not optimal.

## Parameters

- `keyset`: The  , created by the   class method  .

## See Also

- [init(capacity: Int)](nsmutabledictionary/init(capacity:).md)
  Initializes a newly allocated mutable dictionary, allocating enough memory to hold `numItems` entries.
- [init()](nsmutabledictionary/init.md)
  Initializes a newly allocated mutable dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledictionary/init(sharedkeyset:))*