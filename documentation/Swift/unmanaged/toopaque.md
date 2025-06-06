# toOpaque()

**Framework**: Swift  
**Kind**: method

Unsafely converts an unmanaged class reference to a pointer.

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
func toOpaque() -> UnsafeMutableRawPointer
```

#### Return Value

An opaque pointer to the value of this unmanaged reference.

#### Discussion

This operation does not change reference counts.

```swift
let str0 = "boxcar" as CFString
let bits = Unmanaged.passUnretained(str0)
let ptr = bits.toOpaque()
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unmanaged/toopaque())*