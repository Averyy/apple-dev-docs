# withUnsafeMutableBytes(_:)

**Framework**: Swift  
**Kind**: method

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.1+
- watchOS 5.2+

## Declaration

```swift
mutating func withUnsafeMutableBytes<E, Result>(_ body: (UnsafeMutableRawBufferPointer) throws(E) -> Result) throws(E) -> Result where E : Error, Result : ~Copyable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablerawspan/withunsafemutablebytes(_:))*