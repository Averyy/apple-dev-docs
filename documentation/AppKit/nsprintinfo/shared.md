# shared

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The shared printing information object.

**Availability**:
- macOS

## Declaration

```swift
class var shared: NSPrintInfo { get set }
```

```objc
@property (class, strong) NSPrintInfo * sharedPrintInfo;
```

#### Return Value

The shared printer information.

## See Also

### Creating the Printing Information Object
- [init(dictionary: [NSPrintInfo.AttributeKey : Any])](./init%28dictionary%29.md)
  Returns a printing information object initialized with the parameters in the specified dictionary.
- [convenience init()](./init%28%29.md)
  Creates a printing information object.
- [init(coder: NSCoder)](./init%28coder%29.md)
  Creates a printing information object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/shared)*