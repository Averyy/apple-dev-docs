# write(to:)

**Framework**: Foundation  
**Kind**: method

Writes the URL to the specified pasteboard.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func write(to pasteBoard: NSPasteboard)
```

#### Discussion

You must declare an `NSURLPboardType` data type for the pasteboard before invoking this method. Otherwise, the method returns without doing anything.

## Parameters

- `pasteBoard`: The target pasteboard.

## See Also

- [func declareTypes(_ newTypes: [NSPasteboard.PasteboardType], owner newOwner: Any?) -> Int](../AppKit/NSPasteboard/declareTypes(_:owner:).md)
  Prepares the receiver for a change in its contents by declaring the new types of data it will contain and a new owner.
- [init?(fromPasteboard: NSPasteboard)](nsurl/init(frompasteboard:).md)
  Reads an NSURL object off of the specified pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/write(to:))*