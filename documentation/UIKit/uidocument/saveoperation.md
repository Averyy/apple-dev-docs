# UIDocument.SaveOperation

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the type of save operation.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
enum SaveOperation
```

```c
enum UIDocumentSaveOperation : NSInteger;
```

#### Overview

You specify one of these constants as a parameter in the following methods: [`save(to:for:completionHandler:)`](./save%28to,for,completionhandler%29.md), [`writeContents(_:andAttributes:safelyTo:for:)`](./writecontents%28_,andattributes,safelyto,for%29.md), [`writeContents(_:to:for:originalContentsURL:)`](./writecontents%28_,to,for,originalcontentsurl%29.md), [`fileAttributesToWrite(to:for:)`](./fileattributestowrite%28to,for%29.md), [`fileNameExtension(forType:saveOperation:)`](./filenameextension%28fortype,saveoperation%29.md), [`changeCountToken(for:)`](./changecounttoken%28for%29.md), and [`updateChangeCount(withToken:for:)`](./updatechangecount%28withtoken,for%29.md).

## Topics

### Constants
- [UIDocument.SaveOperation.forCreating](./saveoperation/forcreating.md)
  The document is being saved for the first time.
- [UIDocument.SaveOperation.forOverwriting](./saveoperation/foroverwriting.md)
  The document is being saved by overwriting the current version.
### Initializers
- [init?(rawValue: Int)](./saveoperation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [UIDocument.ChangeKind](./changekind.md)
  Constants that specify the kind of change to a document.
- [UIDocument.State](./state.md)
  Constants that specify the document state.
- [class let userActivityURLKey: String](./useractivityurlkey.md)
  The key that identifies the document associated with a user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/saveoperation)*