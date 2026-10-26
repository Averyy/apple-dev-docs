# instantiateNibWithOwner:topLevelObjects:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Unarchives and instantiates the in-memory contents of the receiver’s nib file, creating a distinct object tree and set of top level objects.

**Availability**:
- macOS 10.3+ - Deprecated in 10.8

> **Deprecated**: Use [`instantiate(withOwner:topLevelObjects:)`](./instantiate%28withowner,toplevelobjects%29.md) instead.

## Declaration

```objc
- (BOOL) instantiateNibWithOwner:(id) owner topLevelObjects:(NSArray **) topLevelObjects;
```

#### Return Value

[`true`](../../Swift/true.md) if the nib file’s contents were instantiated successfully; otherwise, [`false`](../../Swift/false.md).

#### Discussion

You may use this method to instantiate a nib file multiple times. This is a convenience method that composes the name-table dictionary and invokes the [`instantiateNibWithExternalNameTable:`](./instantiatenibwithexternalnametable_.md) method, passing it the name table.

## Parameters

- `owner`: The object to use as the owner of the nib file. If the nib file has an owner, you must specify a valid object for this parameter.
- `topLevelObjects`: On input, a variable capable of holding an `NSArray` object. On output, this variable contains an autoreleased `NSArray` object containing the top-level objects from the nib file. You may specify `nil` for this parameter if you are not interested in the top-level objects.

## See Also

### Deprecated
- [- initWithContentsOfURL:](./initwithcontentsofurl_.md)
  Returns an `NSNib` object initialized to the nib file at the specified URL.
- [- instantiateNibWithExternalNameTable:](./instantiatenibwithexternalnametable_.md)
  Unarchives and instantiates the in-memory contents of the receiver’s nib file, creating a distinct object tree and top level objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsnib/instantiatenibwithowner:toplevelobjects:)*