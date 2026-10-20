# contents

**Framework**: File Provider  
**Kind**: property  
**Role**: Type Property

The item’s content.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static var contents: NSFileProviderItemFields { get }
```

```c
NSFileProviderItemContents
```

#### Discussion

If the item is a directory, the content are the item’s children. If the item is a file, the content is the data saved on disk.

## See Also

### Specifying the Required Fields
- [static var filename: NSFileProviderItemFields](./filename.md)
  The item’s filename.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemfields/contents)*