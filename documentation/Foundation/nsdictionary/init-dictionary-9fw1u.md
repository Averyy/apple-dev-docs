# init(dictionary:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly allocated dictionary by placing in it the keys and values contained in another given dictionary.

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
convenience init(dictionary otherDictionary: [AnyHashable : Any])
```

#### Return Value

An initialized dictionary—which might be different than the original receiver—containing the keys and values found in `otherDictionary`.

## Parameters

- `otherDictionary`: A dictionary containing the keys and values with which to initialize the new dictionary.

## See Also

- [convenience init(dictionary: [AnyHashable : Any], copyItems: Bool)](nsdictionary/init(dictionary:copyitems:).md)
  Initializes a newly allocated dictionary using the objects contained in another given dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/init(dictionary:)-9fw1u)*