# source

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The script source for the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var source: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * source;
```

## Discussion

It is possible for an `NSAppleScript` that has been instantiated with [`init(contentsOf:error:)`](./init%28contentsof,error%29.md) to be a script for which the source code is not available but is nonetheless executable.

## See Also

### Getting Information About a Script
- [var isCompiled: Bool](./iscompiled.md)
  A Boolean value that indicates whether the receiver’s script has been compiled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsapplescript/source)*