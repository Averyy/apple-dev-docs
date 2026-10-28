# init(data:filename:typeIdentifier:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a new file object with the specified data and identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(data: Data, filename: String, typeIdentifier: String?)
```

```objc
+ (INFile *) fileWithData:(NSData *) data filename:(NSString *) filename typeIdentifier:(NSString *) typeIdentifier;
```

## Return Value

A new [`INFile`](../infile.md) object containing the supplied information.

## Parameters

- `data`: The data associated with the file.
- `filename`: The name of the file.
- `typeIdentifier`: The type associated with the file.

## See Also

### Initializing a File Object
- [init(fileURL: URL, filename: String?, typeIdentifier: String?)](./init%28fileurl,filename,typeidentifier%29.md)
  Creates a new file object with the specified URL and identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/infile/init(data:filename:typeidentifier:))*