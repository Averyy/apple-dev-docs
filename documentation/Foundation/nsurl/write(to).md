# write(to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Writes the URL to the specified pasteboard.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func write(to pasteBoard: NSPasteboard)
```

```objc
- (void) writeToPasteboard:(NSPasteboard *) pasteBoard;
```

## Discussion

You must declare an `NSURLPboardType` data type for the pasteboard before invoking this method. Otherwise, the method returns without doing anything.

## Parameters

- `pasteBoard`: The target pasteboard.

## See Also

### Related Documentation
- [func declareTypes([NSPasteboard.PasteboardType], owner: Any?) -> Int](../../AppKit/nspasteboard/declaretypes%28_,owner%29.md)
  Prepares the receiver for a change in its contents by declaring the new types of data it will contain and a new owner.
### Working with Pasteboards
- [init?(fromPasteboard: NSPasteboard)](./init%28frompasteboard%29.md)
  Reads an NSURL object off of the specified pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/write(to:))*