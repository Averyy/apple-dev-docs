# write(_:language:to:)

**Framework**: Natural Language  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (BOOL) writeGazetteerForDictionary:(NSDictionary<NSString *,NSArray<NSString *> *> *) dictionary language:(NLLanguage) language toURL:(NSURL *) url error:(NSError **) error;
```

## Parameters

- `dictionary`: The dictionary of labels and an array of terms for each label.
- `language`: The language of the text in the dictionary.
- `url`: The location in the file system to which the file should be written.

## See Also

### Creating a Gazetteer
- [init(contentsOf: URL) throws](./init%28contentsof%29.md)
  Creates a Natural Language gazetteer from a model created with the Create ML framework.
- [init(data: Data) throws](./init%28data%29.md)
  Creates a gazetteer from a data instance.
- [init(dictionary: [String : [String]], language: NLLanguage?) throws](./init%28dictionary,language%29.md)
  Creates a gazetteer from a set of labels for terms represented by a dictionary.
- [+ gazetteerWithContentsOfURL:error:](./gazetteerwithcontentsofurl_error_.md)
  Creates a Natural Language gazetteer from a model created with the Create ML framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlgazetteer/write(_:language:to:))*