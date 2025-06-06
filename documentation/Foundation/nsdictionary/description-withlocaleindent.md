# description(withLocale:indent:)

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
func description(withLocale locale: Any?, indent level: Int) -> String
```

#### Return Value

A string object that represents the contents of the dictionary, formatted as a property list.

#### Discussion

The returned `NSString` object contains the string representations of each of the dictionary’s entries. [`description(withLocale:indent:)`](nsdictionary/description(withlocale:indent:).md) obtains the string representation of a given key or value as follows:

- If the object is an `NSString` object, it is used as is.
- If the object responds to `descriptionWithLocale:indent:`, that method is invoked to obtain the object’s string representation.
- If the object responds to `descriptionWithLocale:`, that method is invoked to obtain the object’s string representation.
- If none of the above conditions is met, the object’s string representation is obtained by through its `description` property.

If each key in the dictionary responds to `compare:`, the entries are listed in ascending order, by key. Otherwise, the order in which the entries are listed is undefined.

## Parameters

- `locale`: On iOS and macOS 10.5 and later, either an instance of   or an   object may be used for  . In OS X v10.4 and earlier it must be an instance of  .
- `level`: Specifies a level of indentation, to make the output more readable: the indentation is (4 spaces) *  .

## See Also

- [var description: String](nsdictionary/description.md)
  A string that represents the contents of the dictionary, formatted as a property list.
- [var descriptionInStringsFileFormat: String](nsdictionary/descriptioninstringsfileformat.md)
  A string that represents the contents of the dictionary, formatted in `.strings` file format.
- [func description(withLocale: Any?) -> String](nsdictionary/description(withlocale:).md)
  Returns a string object that represents the contents of the dictionary, formatted as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/description(withlocale:indent:))*