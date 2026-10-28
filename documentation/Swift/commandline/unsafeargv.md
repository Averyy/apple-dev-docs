# unsafeArgv

**Framework**: Swift  
**Kind**: property  
**Role**: Type Property

Access to the raw argv value from C.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var unsafeArgv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?> { get }
```

## Discussion

The value of this property is a `nil`-terminated C array. Including the trailing `nil`, there are [`argc`](./argc.md) `+ 1` elements in the array.

> **Note**: Accessing the argument vector through this pointer is unsafe. Where possible, use [`arguments`](./arguments.md) instead.

## See Also

### Accessing Raw Argument Data
- [static var argc: Int32](./argc.md)
  Access to the raw argc value from C.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/commandline/unsafeargv)*