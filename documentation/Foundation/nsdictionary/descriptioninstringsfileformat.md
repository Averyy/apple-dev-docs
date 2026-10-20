# descriptionInStringsFileFormat

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly) NSString * descriptionInStringsFileFormat;
```

#### Discussion

The order in which the entries are listed is undefined.

This method fails unless the dictionary can be represented by a strings resource file. For details, see [String Resources](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Strings/Strings.html#//apple_ref/doc/uid/10000051i-CH6) in [Resource Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Introduction/Introduction.html#//apple_ref/doc/uid/10000051i).

## See Also

### Describing a Dictionary
- [var description: String](./description.md)
  A string that represents the contents of the dictionary, formatted as a property list.
- [func description(withLocale: Any?) -> String](./description%28withlocale%29.md)
  Returns a string object that represents the contents of the dictionary, formatted as a property list.
- [func description(withLocale: Any?, indent: Int) -> String](./description%28withlocale,indent%29.md)
  Returns a string object that represents the contents of the dictionary, formatted as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/descriptioninstringsfileformat)*