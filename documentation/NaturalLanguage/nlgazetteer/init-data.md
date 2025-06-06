# init(data:)

**Framework**: Natural Language  
**Kind**: init

Creates a gazetteer from a data instance.

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
init(data: Data) throws
```

## Parameters

- `data`: A gazetteer contained in a data instance.

## See Also

- [init(contentsOf: URL) throws](nlgazetteer/init(contentsof:).md)
  Creates a Natural Language gazetteer from a model created with the Create ML framework.
- [init(dictionary: [String : [String]], language: NLLanguage?) throws](nlgazetteer/init(dictionary:language:).md)
  Creates a gazetteer from a set of labels for terms represented by a dictionary.
- [class func write([String : [String]], language: NLLanguage?, to: URL) throws](nlgazetteer/write(_:language:to:).md)
  Creates a gazetteer from a set of labels for terms represented by a dictionary and saves the gazetteer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlgazetteer/init(data:))*