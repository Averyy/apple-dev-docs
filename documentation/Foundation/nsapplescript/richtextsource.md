# richTextSource

**Framework**: Foundation  
**Kind**: property

Returns the syntax-highlighted source code of the receiver if the receiver has been compiled and its source code is available.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var richTextSource: NSAttributedString? { get }
```

#### Discussion

Returns `nil` otherwise. It is possible for an instance of `NSAppleScript` that has been instantiated with [`init(contentsOf:error:)`](nsapplescript/init(contentsof:error:).md) to be a script for which the source code is not available, but is nonetheless executable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsapplescript/richtextsource)*