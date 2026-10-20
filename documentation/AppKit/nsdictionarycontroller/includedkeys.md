# includedKeys

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The key names that are represented by a key-value pair, even if they are not present in the receiver’s content dictionary.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var includedKeys: [String] { get set }
```

```objc
@property (copy) NSArray<NSString *> * includedKeys;
```

## See Also

### Keys to Display
- [var excludedKeys: [String]](./excludedkeys.md)
  The key names that are never displayed in the user interface items bound to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdictionarycontroller/includedkeys)*