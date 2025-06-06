# export(to:previewImage:)

**Framework**: ARKit  
**Kind**: method

Writes a binary representation of the object to the specified file URL.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func export(to url: URL, previewImage: UIImage?) throws
```

#### Discussion

After exporting a reference object from your object-scanning app to a file, you can bundle that reference object into other apps you create by inserting it into an Xcode asset catalog.

## Parameters

- `url`: The file URL at which to write the reference object data.
- `previewImage`: ARKit ignores preview images when loading reference objects. Instead, this image helps make reference object files visually identifiable in external tools like Xcode, Finder, and Quick Look.

## See Also

- [class let archiveExtension: String](arreferenceobject/archiveextension.md)
  The standard filename extension for exported [`ARReferenceObject`](arreferenceobject.md) instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceobject/export(to:previewimage:))*