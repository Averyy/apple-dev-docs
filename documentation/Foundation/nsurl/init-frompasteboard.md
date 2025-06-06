# init(fromPasteboard:)

**Framework**: Foundation  
**Kind**: init

Reads an NSURL object off of the specified pasteboard.

**Availability**:
- macOS 10.0+

## Declaration

```swift
init?(from pasteBoard: NSPasteboard)
```

#### Return Value

A `NSURL` object, or `nil` if the pasteboard does not contain `NSURLPboardType` data.

## Parameters

- `pasteBoard`: The target pasteboard.

## See Also

- [func write(to: NSPasteboard)](nsurl/write(to:).md)
  Writes the URL to the specified pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/init(frompasteboard:))*