# loadNibFile:externalNameTable:withZone:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Unarchives the contents of the nib file and links them to objects in your program.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

> **Deprecated**: Use the [`loadNibNamed(_:owner:topLevelObjects:)`](../bundle/loadnibnamed%28_,owner,toplevelobjects%29.md) method instead.

## Declaration

```objc
+ (BOOL) loadNibFile:(NSString *) fileName externalNameTable:(NSDictionary *) context withZone:(NSZone *) zone;
```

#### Return Value

[`true`](../../Swift/true.md) if the nib file was loaded successfully; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `fileName`: The location of the nib file specified as an absolute path in the file system.
- `context`: A name table whose keys identify objects associated with your program or the nib file. The newly unarchived objects from the nib file use this table to connect to objects in your program. For example,  the nib file uses the object associated with the `NSNibOwner` constant as the nib file’s owning object. If you associate an empty `NSMutableArray` object with the `NSNibTopLevelObjects` constant, on output, the array contains the top level objects from the nib file. For descriptions of these constants, see [`NSNib`](../../AppKit/nsnib.md).
- `zone`: The memory zone in which to allocate the nib file objects.

## See Also

### Loading nib files
- [func loadNibNamed(String, owner: Any?, options: [UINib.OptionsKey : Any]?) -> [Any]?](../bundle/loadnibnamed%28_,owner,options%29.md)
  Unarchives the contents of a nib file located in the receiver’s bundle.
- [func loadNibNamed(NSNib.Name, owner: Any?, topLevelObjects: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> Bool](../bundle/loadnibnamed%28_,owner,toplevelobjects%29.md)
  Loads a nib from the bundle with the specified file name and owner.
- [+ loadNibNamed:owner:](./loadnibnamed_owner_.md)
  Unarchives the contents of the nib file and links them to a specific owner object.
- [- loadNibFile:externalNameTable:withZone:](./loadnibfile_externalnametable_withzone_-c.method.md)
  Unarchives the contents of a nib file located in the receiver’s bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundle/loadnibfile:externalnametable:withzone:-c.type.method)*