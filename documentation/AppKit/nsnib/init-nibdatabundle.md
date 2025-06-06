# init(nibData:bundle:)

**Framework**: AppKit  
**Kind**: init

Initializes an instance with nib data and specified bundle for locating resources.

**Availability**:
- macOS 10.8+

## Declaration

```swift
init(nibData: Data, bundle: Bundle?)
```

#### Return Value

The initialized `NSNib` object or `nil` if there were errors during initialization.

## Parameters

- `nibData`: The nib data.
- `bundle`: The bundle for locating resources. If  , the main application bundle is used.

## See Also

- [init?(nibNamed: NSNib.Name, bundle: Bundle?)](nsnib/init(nibnamed:bundle:).md)
  Returns an `NSNib` object initialized to the nib file in the specified bundle.
- [typealias Name](nsnib/name.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsnib/init(nibdata:bundle:))*