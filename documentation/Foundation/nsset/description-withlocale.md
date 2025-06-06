# description(withLocale:)

**Framework**: Foundation  
**Kind**: method

Returns a string that represents the contents of the set, formatted as a property list.

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
func description(withLocale locale: Any?) -> String
```

#### Return Value

A string that represents the contents of the set, formatted as a property list.

#### Discussion

This method sends each of the set’s members  `descriptionWithLocale:` with `locale` passed as the sole parameter. If the set’s members do not respond to `descriptionWithLocale:`, this method sends [`description`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/description) instead.

## Parameters

- `locale`: On iOS and macOS 10.5 and later, either an instance of   or an   object may be used for  .In OS X v10.4 and earlier it must be an instance of  .

## See Also

- [var description: String](nsset/description.md)
  A string that represents the contents of the set, formatted as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/description(withlocale:))*