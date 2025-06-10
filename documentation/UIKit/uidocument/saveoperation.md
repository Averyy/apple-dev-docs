# UIDocument.SaveOperation

**Framework**: UIKit  
**Kind**: enum

Constants that specify the type of save operation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
enum SaveOperation
```

#### Overview

You specify one of these constants as a parameter in the following methods: [`save(to:for:completionHandler:)`](uidocument/save(to:for:completionhandler:).md), [`writeContents(_:andAttributes:safelyTo:for:)`](uidocument/writecontents(_:andattributes:safelyto:for:).md), [`writeContents(_:to:for:originalContentsURL:)`](uidocument/writecontents(_:to:for:originalcontentsurl:).md), [`fileAttributesToWrite(to:for:)`](uidocument/fileattributestowrite(to:for:).md), [`fileNameExtension(forType:saveOperation:)`](uidocument/filenameextension(fortype:saveoperation:).md), [`changeCountToken(for:)`](uidocument/changecounttoken(for:).md), and [`updateChangeCount(withToken:for:)`](uidocument/updatechangecount(withtoken:for:).md).

## Topics

### Constants
- [UIDocument.SaveOperation.forCreating](uidocument/saveoperation/forcreating.md)
  The document is being saved for the first time.
- [UIDocument.SaveOperation.forOverwriting](uidocument/saveoperation/foroverwriting.md)
  The document is being saved by overwriting the current version.
### Initializers
- [init?(rawValue: Int)](uidocument/saveoperation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [UIDocument.ChangeKind](uidocument/changekind.md)
  Constants that specify the kind of change to a document.
- [UIDocument.State](uidocument/state.md)
  Constants that specify the document state.
- [class let userActivityURLKey: String](uidocument/useractivityurlkey.md)
  The key that identifies the document associated with a user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/saveoperation)*