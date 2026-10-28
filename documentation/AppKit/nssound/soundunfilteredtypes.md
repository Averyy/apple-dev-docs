# soundUnfilteredTypes

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Provides the file types the `NSSound` class understands.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class var soundUnfilteredTypes: [String] { get }
```

```objc
@property (class, copy, readonly) NSArray<NSString *> * soundUnfilteredTypes;
```

## Return Value

Array of UTIs identifying the file types the `NSSound` class understands.

## See Also

### Getting Sound Information
- [init?(named: NSSound.Name)](./init%28named%29.md)
  Returns the `NSSound` instance associated with a given name.
- [var duration: TimeInterval](./duration.md)
  The duration of the sound, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/soundunfilteredtypes)*