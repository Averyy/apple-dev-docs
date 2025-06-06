# source

**Framework**: Foundation  
**Kind**: property

The script source for the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var source: String? { get }
```

#### Discussion

It is possible for an `NSAppleScript` that has been instantiated with [`init(contentsOf:error:)`](nsapplescript/init(contentsof:error:).md) to be a script for which the source code is not available but is nonetheless executable.

## See Also

- [var isCompiled: Bool](nsapplescript/iscompiled.md)
  A Boolean value that indicates whether the receiver’s script has been compiled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsapplescript/source)*