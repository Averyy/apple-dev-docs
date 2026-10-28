# initWithContentsOfURL:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an `NSNib` object initialized to the nib file at the specified URL.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

> **Deprecated**: Use [`init(nibData:bundle:)`](./init%28nibdata,bundle%29.md) and specify a bundle for locating images and other resources.

## Declaration

```objc
- (id) initWithContentsOfURL:(NSURL *) nibFileURL;
```

## Return Value

The initialized `NSNib` object or `nil` if there were errors during initialization or the nib file could not be located.

## Discussion

When you instantiate the nib objects later, the `NSNib` object looks for an appropriate bundle from which to search for any additional resources referenced by the nib. Because you do not specify a bundle directory when calling this method, the receiver uses the bundle associated with the class of the nib file’s owner. If the nib file does not have an owner, the receiver uses the application’s main bundle instead.

## Parameters

- `nibFileURL`: The location of the nib file.

## See Also

### Related Documentation
- [Resource Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Introduction/Introduction.html#//apple_ref/doc/uid/10000051i)
### Deprecated
- [- instantiateNibWithOwner:topLevelObjects:](./instantiatenibwithowner_toplevelobjects_.md)
  Unarchives and instantiates the in-memory contents of the receiver’s nib file, creating a distinct object tree and set of top level objects.
- [- instantiateNibWithExternalNameTable:](./instantiatenibwithexternalnametable_.md)
  Unarchives and instantiates the in-memory contents of the receiver’s nib file, creating a distinct object tree and top level objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsnib/initwithcontentsofurl:)*