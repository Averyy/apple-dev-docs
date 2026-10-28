# init(docFormat:documentAttributes:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates an attributed string from Microsoft Word format data in the specified data object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
init?(docFormat data: Data, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

```objc
- (instancetype) initWithDocFormat:(NSData *) data documentAttributes:(NSDictionary<NSString *,id> **) dict;
```

## Return Value

Returns an initialized attributed string object, or `nil` if the method can’t decode the data.

## Parameters

- `data`: The data from which to create the string.
- `dict`: An in-out dictionary containing document-level attributes. On output, this method updates the dictionary to contain any document-specific keys found in the data. Specify `nil` if you don’t want the document attributes.

## See Also

### Creating from a data file
- [init(data: Data, options: [NSAttributedString.DocumentReadingOptionKey : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](./init%28data,options,documentattributes%29.md)
  Creates an attributed string from the contents of the specified data object.
- [init(URL: URL, options: [NSAttributedString.DocumentReadingOptionKey : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](./init%28url,options,documentattributes%29.md)
  Creates an attributed string from the contents of the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(docformat:documentattributes:))*