# description(withLocale:indent:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSString *) descriptionWithLocale:(id) locale indent:(NSUInteger) level;
```

## Return Value

A string object that represents the contents of the dictionary, formatted as a property list.

## Discussion

The returned `NSString` object contains the string representations of each of the dictionary’s entries. [`description(withLocale:indent:)`](./description%28withlocale,indent%29.md) obtains the string representation of a given key or value as follows:

- If the object is an `NSString` object, it is used as is.
- If the object responds to `descriptionWithLocale:indent:`, that method is invoked to obtain the object’s string representation.
- If the object responds to `descriptionWithLocale:`, that method is invoked to obtain the object’s string representation.
- If none of the above conditions is met, the object’s string representation is obtained by through its `description` property.

If each key in the dictionary responds to `compare:`, the entries are listed in ascending order, by key. Otherwise, the order in which the entries are listed is undefined.

## Parameters

- `locale`: An object that specifies options used for formatting each of the dictionary’s keys and values; pass `nil` if you don’t want them formatted.

  On iOS and macOS 10.5 and later, either an instance of `NSDictionary` or an `NSLocale` object may be used for `locale`. In OS X v10.4 and earlier it must be an instance of `NSDictionary`.
- `level`: Specifies a level of indentation, to make the output more readable: the indentation is (4 spaces) * `level`.

## See Also

### Describing a Dictionary
- [var description: String](./description.md)
  A string that represents the contents of the dictionary, formatted as a property list.
- [var descriptionInStringsFileFormat: String](./descriptioninstringsfileformat.md)
  A string that represents the contents of the dictionary, formatted in `.strings` file format.
- [func description(withLocale: Any?) -> String](./description%28withlocale%29.md)
  Returns a string object that represents the contents of the dictionary, formatted as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/description(withlocale:indent:))*