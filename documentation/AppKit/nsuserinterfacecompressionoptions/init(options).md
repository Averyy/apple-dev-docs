# init(options:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates an option object that represents the union of the supplied options.

**Availability**:
- macOS 10.13+

## Declaration

```swift
init(options: Set<NSUserInterfaceCompressionOptions>)
```

```objc
- (instancetype) initWithCompressionOptions:(NSSet<NSUserInterfaceCompressionOptions *> *) options;
```

## Parameters

- `options`: A set of [`NSUserInterfaceCompressionOptions`](../nsuserinterfacecompressionoptions.md) objects.

## See Also

### Creating a compression option
- [init()](./init%28%29.md)
  Creates an option object containing no options.
- [init(identifier: String)](./init%28identifier%29.md)
  Creates an option object with the given identifier string.
- [init(coder: NSCoder)](./init%28coder%29.md)
  Creates an option object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacecompressionoptions/init(options:))*