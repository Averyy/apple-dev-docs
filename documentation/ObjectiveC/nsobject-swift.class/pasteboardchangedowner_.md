# pasteboardChangedOwner:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Notifies a prior owner of the specified pasteboard (and owners of representations on the pasteboard) that the pasteboard has changed owners.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

## Declaration

```objc
- (void) pasteboardChangedOwner:(NSPasteboard *) sender;
```

## Discussion

Pasteboard owners only need to implement this method if they need to know when they have lost ownership.

The owner is not able to read the contents of the pasteboard when responding to this method. The owner should be prepared to receive this method at any time, even from within the [`declareTypes(_:owner:)`](../../AppKit/nspasteboard/declaretypes%28_,owner%29.md) method used to declare ownership.

Once an owner has provided all of its data for declared types, it will not receive a `pasteboardChangedOwner:` message. If, therefore, you are maintaining an object just for the purpose of providing data lazily, rather than relying solely on receipt of a `pasteboardChangedOwner:` message you need to keep track of what types were promised and what types have been provided. When all the types have been provided, you may release the owner.

## Parameters

- `sender`: The pasteboard object whose owner changed.

## See Also

### Related Documentation
- [var changeCount: Int](../../AppKit/nspasteboard/changecount.md)
  The receiver’s change count.
- [func declareTypes([NSPasteboard.PasteboardType], owner: Any?) -> Int](../../AppKit/nspasteboard/declaretypes%28_,owner%29.md)
  Prepares the receiver for a change in its contents by declaring the new types of data it will contain and a new owner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/pasteboardchangedowner:)*