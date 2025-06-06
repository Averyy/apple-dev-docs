# write(_:language:to:)

**Framework**: Natural Language  
**Kind**: method

Creates a gazetteer from a set of labels for terms represented by a dictionary and saves the gazetteer to a file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func write(_ dictionary: [String : [String]], language: NLLanguage?, to url: URL) throws
```

## Parameters

- `dictionary`: The dictionary of labels and an array of terms for each label.
- `language`: The language of the text in the dictionary.
- `url`: The location in the file system to which the file should be written.

## See Also

- [init(contentsOf: URL) throws](nlgazetteer/init(contentsof:).md)
  Creates a Natural Language gazetteer from a model created with the Create ML framework.
- [init(data: Data) throws](nlgazetteer/init(data:).md)
  Creates a gazetteer from a data instance.
- [init(dictionary: [String : [String]], language: NLLanguage?) throws](nlgazetteer/init(dictionary:language:).md)
  Creates a gazetteer from a set of labels for terms represented by a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlgazetteer/write(_:language:to:))*