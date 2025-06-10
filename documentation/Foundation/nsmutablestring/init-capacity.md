# init(capacity:)

**Framework**: Foundation  
**Kind**: init

Returns an `NSMutableString` object initialized with initial storage for a given number of characters,

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(capacity: Int)
```

#### Return Value

An initialized `NSMutableString` object with initial storage for `capacity` characters. The returned object might be different than the original receiver.

#### Discussion

The number of characters indicated by `capacity` is simply a hint to increase the efficiency of data storage. The value does  limit the length of the string.

## Parameters

- `capacity`: The number of characters the string is expected to initially contain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablestring/init(capacity:))*