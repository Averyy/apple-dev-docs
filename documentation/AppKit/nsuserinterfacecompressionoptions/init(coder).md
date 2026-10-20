# init(coder:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates an option object from data in an unarchiver.

**Availability**:
- macOS 10.13+

## Declaration

```swift
init(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## See Also

### Creating a compression option
- [init()](./init%28%29.md)
  Creates an option object containing no options.
- [init(options: Set<NSUserInterfaceCompressionOptions>)](./init%28options%29.md)
  Creates an option object that represents the union of the supplied options.
- [init(identifier: String)](./init%28identifier%29.md)
  Creates an option object with the given identifier string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacecompressionoptions/init(coder:))*