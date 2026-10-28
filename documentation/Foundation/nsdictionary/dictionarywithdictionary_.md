# dictionaryWithDictionary:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates a dictionary containing the keys and values from another given dictionary.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) dictionaryWithDictionary:(NSDictionary<id,id> *) dict;
```

## Return Value

A new dictionary containing the keys and values found in `dict`.

## Parameters

- `dict`: A dictionary containing the keys and values with which to initialize the new dictionary.

## See Also

### Creating a Dictionary from Another Dictionary
- [convenience init(dictionary: [AnyHashable : Any])](./init%28dictionary%29-9fw1u.md)
  Initializes a newly allocated dictionary by placing in it the keys and values contained in another given dictionary.
- [convenience init(dictionary: [AnyHashable : Any], copyItems: Bool)](./init%28dictionary,copyitems%29.md)
  Initializes a newly allocated dictionary using the objects contained in another given dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/dictionarywithdictionary:)*