# archiveExtension

**Framework**: ARKit  
**Kind**: property

The standard filename extension for exported [`ARReferenceObject`](arreferenceobject.md) instances.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class let archiveExtension: String
```

#### Discussion

Use this filename extension when constructing a URL to save a reference object file with the [`export(to:previewImage:)`](arreferenceobject/export(to:previewimage:).md) method.

## See Also

- [func export(to: URL, previewImage: UIImage?) throws](arreferenceobject/export(to:previewimage:).md)
  Writes a binary representation of the object to the specified file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceobject/archiveextension)*