# gazetteerWithContentsOfURL:error:

**Framework**: Natural Language  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (instancetype) gazetteerWithContentsOfURL:(NSURL *) url error:(NSError **) error;
```

## Discussion

Use this initializer to create an [`NLGazetteer`](../nlgazetteer.md) from an `.mlmodel` file saved by [`MLGazetteer`](../../CreateML/mlgazetteer.md) in the `Create ML` framework.

## Parameters

- `url`: The location of the .`mlmodel` file that contains a gazetteer.

## See Also

### Creating a Gazetteer
- [init(contentsOf: URL) throws](./init%28contentsof%29.md)
  Creates a Natural Language gazetteer from a model created with the Create ML framework.
- [init(data: Data) throws](./init%28data%29.md)
  Creates a gazetteer from a data instance.
- [init(dictionary: [String : [String]], language: NLLanguage?) throws](./init%28dictionary,language%29.md)
  Creates a gazetteer from a set of labels for terms represented by a dictionary.
- [class func write([String : [String]], language: NLLanguage?, to: URL) throws](./write%28_,language,to%29.md)
  Creates a gazetteer from a set of labels for terms represented by a dictionary and saves the gazetteer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlgazetteer/gazetteerwithcontentsofurl:error:)*