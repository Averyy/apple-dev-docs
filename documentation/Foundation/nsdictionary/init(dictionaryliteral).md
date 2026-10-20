# init(dictionaryLiteral:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a newly allocated dictionary from the given key-value pairs.

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
required convenience init(dictionaryLiteral elements: (Any, Any)...)
```

## Parameters

- `elements`: A variadic array of two-member tuples, where the first member is a key and the second is its corresponding value.

## See Also

### Creating a Dictionary from Another Dictionary
- [convenience init(dictionary: [AnyHashable : Any])](./init%28dictionary%29-9fw1u.md)
  Initializes a newly allocated dictionary by placing in it the keys and values contained in another given dictionary.
- [convenience init(dictionary: [AnyHashable : Any], copyItems: Bool)](./init%28dictionary,copyitems%29.md)
  Initializes a newly allocated dictionary using the objects contained in another given dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/init(dictionaryliteral:))*