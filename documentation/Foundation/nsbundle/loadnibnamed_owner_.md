# loadNibNamed:owner:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Unarchives the contents of the nib file and links them to a specific owner object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

> **Deprecated**: Use the [`loadNibNamed(_:owner:topLevelObjects:)`](../bundle/loadnibnamed%28_,owner,toplevelobjects%29.md) method instead.

## Declaration

```objc
+ (BOOL) loadNibNamed:(NSString *) nibName owner:(id) owner;
```

## Return Value

[`true`](../../Swift/true.md) if the nib file was loaded successfully; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `nibName`: The name of the nib file, which need not include the `.nib` extension. The file name should not include path information. The object in the `owner` parameter determines the location in which to look for the nib file.
- `owner`: The object to assign as the nib File’s Owner. If the class of this object has an associated bundle, that bundle is searched for the specified nib file; otherwise, this method looks in the main bundle.

## See Also

### Loading nib files
- [func loadNibNamed(String, owner: Any?, options: [UINib.OptionsKey : Any]?) -> [Any]?](../bundle/loadnibnamed%28_,owner,options%29.md)
  Unarchives the contents of a nib file located in the receiver’s bundle.
- [func loadNibNamed(NSNib.Name, owner: Any?, topLevelObjects: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> Bool](../bundle/loadnibnamed%28_,owner,toplevelobjects%29.md)
  Loads a nib from the bundle with the specified file name and owner.
- [+ loadNibFile:externalNameTable:withZone:](./loadnibfile_externalnametable_withzone_-c.type.method.md)
  Unarchives the contents of the nib file and links them to objects in your program.
- [- loadNibFile:externalNameTable:withZone:](./loadnibfile_externalnametable_withzone_-c.method.md)
  Unarchives the contents of a nib file located in the receiver’s bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundle/loadnibnamed:owner:)*