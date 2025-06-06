# description(withLocale:indent:)

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
func description(withLocale locale: Any?, indent level: Int) -> String
```

#### Return Value

A string that represents the contents of the ordered set, formatted as a property list.

#### Discussion

The returned `NSString` object contains the string representations of each of the ordered set’s elements, in order, from first to last. To obtain the string representation of a given element, `descriptionWithLocale:indent:` proceeds as follows:

- If the element is an `NSString` object, it is used as is.
- If the element responds to `descriptionWithLocale:indent:`, that method is invoked to obtain the element’s string representation.
- If the element responds to `descriptionWithLocale:`, that method is invoked to obtain the element’s string representation.
- If none of the above conditions is met, the element’s string representation is obtained by invoking its `description` method

## Parameters

- `locale`: An   object or an   object that specifies options used for formatting each of the array’s elements (where recognized). Specify   if you don’t want the elements formatted.
- `level`: Specifies a level of indentation, to make the output more readable: the indentation is (4 spaces) *  .

## See Also

- [var description: String](nsorderedset/description.md)
  A string that represents the contents of the ordered set, formatted as a property list.
- [func description(withLocale: Any?) -> String](nsorderedset/description(withlocale:).md)
  Returns a string that represents the contents of the ordered set, formatted as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/description(withlocale:indent:))*