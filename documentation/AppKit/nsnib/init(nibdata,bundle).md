# init(nibData:bundle:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes an instance with nib data and specified bundle for locating resources.

**Availability**:
- macOS 10.8+

## Declaration

```swift
init(nibData: Data, bundle: Bundle?)
```

```objc
- (instancetype) initWithNibData:(NSData *) nibData bundle:(NSBundle *) bundle;
```

#### Return Value

The initialized `NSNib` object or `nil` if there were errors during initialization.

## Parameters

- `nibData`: The nib data.
- `bundle`: The bundle for locating resources. If `nil`, the main application bundle is used.

## See Also

### Initializing a Nib
- [init?(nibNamed: NSNib.Name, bundle: Bundle?)](./init%28nibnamed,bundle%29.md)
  Returns an `NSNib` object initialized to the nib file in the specified bundle.
- [typealias Name](./name.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsnib/init(nibdata:bundle:))*