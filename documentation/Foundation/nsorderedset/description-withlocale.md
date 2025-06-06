# description(withLocale:)

**Framework**: Foundation  
**Kind**: method

Returns a string that represents the contents of the ordered set, formatted as a property list.

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

A string that represents the contents of the ordered set, formatted as a property list.

#### Discussion

For a description of how locale is applied to each element in the receiving ordered set, see [`description(withLocale:indent:)`](nsorderedset/description(withlocale:indent:).md).

## Parameters

- `locale`: An   object or an   object that specifies options used for formatting each of the ordered set’s elements (where recognized). Specify   if you don’t want the elements formatted.

## See Also

- [var description: String](nsorderedset/description.md)
  A string that represents the contents of the ordered set, formatted as a property list.
- [func description(withLocale: Any?, indent: Int) -> String](nsorderedset/description(withlocale:indent:).md)
  Returns a string that represents the contents of the ordered set, formatted as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/description(withlocale:))*