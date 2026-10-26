# instantiateNibWithExternalNameTable:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Unarchives and instantiates the in-memory contents of the receiver’s nib file, creating a distinct object tree and top level objects.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

> **Deprecated**: Use [`instantiate(withOwner:topLevelObjects:)`](./instantiate%28withowner,toplevelobjects%29.md) instead.

## Declaration

```objc
- (BOOL) instantiateNibWithExternalNameTable:(NSDictionary *) externalNameTable;
```

#### Return Value

[`true`](../../Swift/true.md) if the nib file’s contents were instantiated successfully; otherwise, [`false`](../../Swift/false.md).

#### Discussion

This is the primitive method for performing instantiations of a nib file. You may use this method to instantiate a nib file multiple times. Each instantiation of the nib must have a distinct owner object that is responsible for the resulting object tree.

If the nib file requires an owner, the `externalNameTable` parameter must contain the object representing the nib file’s owner (associated with the `NSNibOwner` key). The parameter may optionally include an `NSMutableArray` object to be populated with the top-level objects nib file (associated with the `NSNibTopLevelObjects` key).

## Parameters

- `externalNameTable`: A dictionary containing entries for the nib file’s owner and top-level objects. See the discussion for more information.

## See Also

### Deprecated
- [- initWithContentsOfURL:](./initwithcontentsofurl_.md)
  Returns an `NSNib` object initialized to the nib file at the specified URL.
- [- instantiateNibWithOwner:topLevelObjects:](./instantiatenibwithowner_toplevelobjects_.md)
  Unarchives and instantiates the in-memory contents of the receiver’s nib file, creating a distinct object tree and set of top level objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsnib/instantiatenibwithexternalnametable:)*