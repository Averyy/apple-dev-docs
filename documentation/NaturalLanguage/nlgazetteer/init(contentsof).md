# init(contentsOf:)

**Framework**: Natural Language  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithContentsOfURL:(NSURL *) url error:(NSError **) error;
```

#### Discussion

Use this initializer to create an [`NLGazetteer`](../nlgazetteer.md) from an `.mlmodel` file saved by [`MLGazetteer`](../../CreateML/mlgazetteer.md) in the `Create ML` framework.

## Parameters

- `url`: The location of the .`mlmodel` file that contains a gazetteer.

## See Also

### Creating a Gazetteer
- [init(data: Data) throws](./init%28data%29.md)
  Creates a gazetteer from a data instance.
- [init(dictionary: [String : [String]], language: NLLanguage?) throws](./init%28dictionary,language%29.md)
  Creates a gazetteer from a set of labels for terms represented by a dictionary.
- [class func write([String : [String]], language: NLLanguage?, to: URL) throws](./write%28_,language,to%29.md)
  Creates a gazetteer from a set of labels for terms represented by a dictionary and saves the gazetteer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlgazetteer/init(contentsof:))*