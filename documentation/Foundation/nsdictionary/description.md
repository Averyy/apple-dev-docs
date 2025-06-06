# description

**Framework**: Foundation  
**Kind**: property

A string that represents the contents of the dictionary, formatted as a property list.

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
var description: String { get }
```

#### Discussion

If each key in the dictionary is an `NSString` object, the entries are listed in ascending order by key, otherwise the order in which the entries are listed is undefined.  This property is intended to produce readable output for debugging purposes, not for serializing data. If you want to store dictionary data for later retrieval, see [`Property List Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i) and [`Archives and Serializations Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i).

## See Also

- [var descriptionInStringsFileFormat: String](nsdictionary/descriptioninstringsfileformat.md)
  A string that represents the contents of the dictionary, formatted in `.strings` file format.
- [func description(withLocale: Any?) -> String](nsdictionary/description(withlocale:).md)
  Returns a string object that represents the contents of the dictionary, formatted as a property list.
- [func description(withLocale: Any?, indent: Int) -> String](nsdictionary/description(withlocale:indent:).md)
  Returns a string object that represents the contents of the dictionary, formatted as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/description)*