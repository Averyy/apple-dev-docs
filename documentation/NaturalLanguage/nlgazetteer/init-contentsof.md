# init(contentsOf:)

**Framework**: Natural Language  
**Kind**: init

Creates a Natural Language gazetteer from a model created with the Create ML framework.

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
init(contentsOf url: URL) throws
```

#### Discussion

Use this initializer to create an [`NLGazetteer`](nlgazetteer.md) from an `.mlmodel` file saved by [`MLGazetteer`](https://developer.apple.com/documentation/CreateML/MLGazetteer) in the `Create ML` framework.

## Parameters

- `url`: The location of the .  file that contains a gazetteer.

## See Also

- [init(data: Data) throws](nlgazetteer/init(data:).md)
  Creates a gazetteer from a data instance.
- [init(dictionary: [String : [String]], language: NLLanguage?) throws](nlgazetteer/init(dictionary:language:).md)
  Creates a gazetteer from a set of labels for terms represented by a dictionary.
- [class func write([String : [String]], language: NLLanguage?, to: URL) throws](nlgazetteer/write(_:language:to:).md)
  Creates a gazetteer from a set of labels for terms represented by a dictionary and saves the gazetteer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlgazetteer/init(contentsof:))*