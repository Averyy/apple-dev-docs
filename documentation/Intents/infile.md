# INFile

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An object that describes a file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INFile
```

```objc
@interface INFile : NSObject
```

## Mentions

- [Improving interactions between Siri and your messaging app](../SiriKit/improving-interactions-between-siri-and-your-messaging-app.md)

## Topics

### Initializing a File Object
- [init(data: Data, filename: String, typeIdentifier: String?)](./infile/init%28data,filename,typeidentifier%29.md)
  Creates a new file object with the specified data and identifier.
- [init(fileURL: URL, filename: String?, typeIdentifier: String?)](./infile/init%28fileurl,filename,typeidentifier%29.md)
  Creates a new file object with the specified URL and identifier.
### Getting the File Information
- [var filename: String](./infile/filename.md)
  The name of the file.
- [var data: Data](./infile/data.md)
  The data associated with a file.
- [var fileURL: URL?](./infile/fileurl.md)
  The URL that describes the location of the file.
- [var typeIdentifier: String?](./infile/typeidentifier.md)
  The type of the file.
### Initializers
- [init?(coder: NSCoder)](./infile/init%28coder%29.md)
### Instance Properties
- [var removedOnCompletion: Bool](./infile/removedoncompletion.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/infile)*