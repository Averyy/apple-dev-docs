# richTextSource

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the syntax-highlighted source code of the receiver if the receiver has been compiled and its source code is available.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var richTextSource: NSAttributedString? { get }
```

```objc
@property (strong, readonly, nullable) NSAttributedString * richTextSource;
```

## Discussion

Returns `nil` otherwise. It is possible for an instance of `NSAppleScript` that has been instantiated with [`init(contentsOf:error:)`](./init%28contentsof,error%29.md) to be a script for which the source code is not available, but is nonetheless executable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsapplescript/richtextsource)*