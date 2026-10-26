# init(dictionary:language:)

**Framework**: Natural Language  
**Kind**: init  
**Role**: Initializer

Creates a gazetteer from a set of labels for terms represented by a dictionary.

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
init(dictionary: [String : [String]], language: NLLanguage?) throws
```

```objc
- (instancetype) initWithDictionary:(NSDictionary<NSString *,NSArray<NSString *> *> *) dictionary language:(NLLanguage) language error:(NSError **) error;
```

## Parameters

- `dictionary`: The dictionary of labels and an array of terms for each label.
- `language`: The language of the text in the dictionary.

## See Also

### Creating a Gazetteer
- [init(contentsOf: URL) throws](./init%28contentsof%29.md)
  Creates a Natural Language gazetteer from a model created with the Create ML framework.
- [init(data: Data) throws](./init%28data%29.md)
  Creates a gazetteer from a data instance.
- [class func write([String : [String]], language: NLLanguage?, to: URL) throws](./write%28_,language,to%29.md)
  Creates a gazetteer from a set of labels for terms represented by a dictionary and saves the gazetteer to a file.
- [+ gazetteerWithContentsOfURL:error:](./gazetteerwithcontentsofurl_error_.md)
  Creates a Natural Language gazetteer from a model created with the Create ML framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlgazetteer/init(dictionary:language:))*