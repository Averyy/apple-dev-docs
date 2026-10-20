# init(data:)

**Framework**: Natural Language  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithData:(NSData *) data error:(NSError **) error;
```

## Parameters

- `data`: A gazetteer contained in a data instance.

## See Also

### Creating a Gazetteer
- [init(contentsOf: URL) throws](./init%28contentsof%29.md)
  Creates a Natural Language gazetteer from a model created with the Create ML framework.
- [init(dictionary: [String : [String]], language: NLLanguage?) throws](./init%28dictionary,language%29.md)
  Creates a gazetteer from a set of labels for terms represented by a dictionary.
- [class func write([String : [String]], language: NLLanguage?, to: URL) throws](./write%28_,language,to%29.md)
  Creates a gazetteer from a set of labels for terms represented by a dictionary and saves the gazetteer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlgazetteer/init(data:))*