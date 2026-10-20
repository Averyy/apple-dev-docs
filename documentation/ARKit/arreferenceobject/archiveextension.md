# archiveExtension

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

The standard filename extension for exported [`ARReferenceObject`](../arreferenceobject.md) instances.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
class let archiveExtension: String
```

```c
extern NSString * const ARReferenceObjectArchiveExtension;
```

#### Discussion

Use this filename extension when constructing a URL to save a reference object file with the [`export(to:previewImage:)`](./export%28to,previewimage%29.md) method.

## See Also

### Saving Recorded Objects
- [func export(to: URL, previewImage: UIImage?) throws](./export%28to,previewimage%29.md)
  Writes a binary representation of the object to the specified file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceobject/archiveextension)*