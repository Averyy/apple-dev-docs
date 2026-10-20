# init(fromPasteboard:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Reads an NSURL object off of the specified pasteboard.

**Availability**:
- macOS 10.0+

## Declaration

```swift
init?(fromPasteboard pasteBoard: NSPasteboard)
```

```swift
init?(from pasteBoard: NSPasteboard)
```

```objc
+ (NSURL *) URLFromPasteboard:(NSPasteboard *) pasteBoard;
```

#### Return Value

A `NSURL` object, or `nil` if the pasteboard does not contain `NSURLPboardType` data.

## Parameters

- `pasteBoard`: The target pasteboard.

## See Also

### Working with Pasteboards
- [func write(to: NSPasteboard)](./write%28to%29.md)
  Writes the URL to the specified pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/init(frompasteboard:))*