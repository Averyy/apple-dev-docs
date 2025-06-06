# descriptionInStringsFileFormat

**Framework**: Foundation  
**Kind**: property

A string that represents the contents of the dictionary, formatted in `.strings` file format.

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
var descriptionInStringsFileFormat: String { get }
```

#### Discussion

The order in which the entries are listed is undefined.

This method fails unless the dictionary can be represented by a strings resource file. For details, see [`String Resources`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Strings/Strings.html#//apple_ref/doc/uid/10000051i-CH6) in [`Resource Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Introduction/Introduction.html#//apple_ref/doc/uid/10000051i).

## See Also

- [var description: String](nsdictionary/description.md)
  A string that represents the contents of the dictionary, formatted as a property list.
- [func description(withLocale: Any?) -> String](nsdictionary/description(withlocale:).md)
  Returns a string object that represents the contents of the dictionary, formatted as a property list.
- [func description(withLocale: Any?, indent: Int) -> String](nsdictionary/description(withlocale:indent:).md)
  Returns a string object that represents the contents of the dictionary, formatted as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/descriptioninstringsfileformat)*