# init(identifier:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates an option object with the given identifier string.

**Availability**:
- macOS 10.13+

## Declaration

```swift
init(identifier: String)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier;
```

#### Discussion

Use this initializer to create custom compression options.

## See Also

### Creating a compression option
- [init()](./init%28%29.md)
  Creates an option object containing no options.
- [init(options: Set<NSUserInterfaceCompressionOptions>)](./init%28options%29.md)
  Creates an option object that represents the union of the supplied options.
- [init(coder: NSCoder)](./init%28coder%29.md)
  Creates an option object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacecompressionoptions/init(identifier:))*