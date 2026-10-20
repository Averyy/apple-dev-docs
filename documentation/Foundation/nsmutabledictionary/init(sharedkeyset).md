# init(sharedKeySet:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (NSMutableDictionary<id,id> *) dictionaryWithSharedKeySet:(id) keyset;
```

#### Return Value

A new mutable dictionary optimized for a known set of keys.

#### Discussion

Keys that are not in the key set can still be set in the dictionary, but that usage is not optimal.

## Parameters

- `keyset`: The `keyset`, created by the [`NSDictionary`](../nsdictionary.md) class method [`sharedKeySet(forKeys:)`](../nsdictionary/sharedkeyset%28forkeys%29.md).

  > ❗ **Important**:  If `keyset` is `nil`, an exception is raised. If `keyset` is not an object returned by [`sharedKeySet(forKeys:)`](../nsdictionary/sharedkeyset%28forkeys%29.md), an exception is raised.

## See Also

### Creating and Initializing a Mutable Dictionary
- [init(capacity: Int)](./init%28capacity%29.md)
  Initializes a newly allocated mutable dictionary, allocating enough memory to hold `numItems` entries.
- [init()](./init%28%29.md)
  Initializes a newly allocated mutable dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledictionary/init(sharedkeyset:))*