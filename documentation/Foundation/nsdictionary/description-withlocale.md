# description(withLocale:)

**Framework**: Foundation  
**Kind**: method

Returns a string object that represents the contents of the dictionary, formatted as a property list.

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

#### Discussion

For a description of how `locale` is applied to each element in the dictionary, see [`description(withLocale:indent:)`](nsdictionary/description(withlocale:indent:).md).

If each key in the dictionary responds to `compare:`, the entries are listed in ascending order by key, otherwise the order in which the entries are listed is undefined.

## Parameters

- `locale`: On iOS and macOS 10.5 and later, either an instance of   or an   object may be used for  . In OS X v10.4 and earlier it must be an instance of  .

## See Also

- [var description: String](nsdictionary/description.md)
  A string that represents the contents of the dictionary, formatted as a property list.
- [var descriptionInStringsFileFormat: String](nsdictionary/descriptioninstringsfileformat.md)
  A string that represents the contents of the dictionary, formatted in `.strings` file format.
- [func description(withLocale: Any?, indent: Int) -> String](nsdictionary/description(withlocale:indent:).md)
  Returns a string object that represents the contents of the dictionary, formatted as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/description(withlocale:))*