# storeBytes(of:toByteOffset:as:)

**Framework**: Swift  
**Kind**: method

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
mutating func storeBytes<T>(of value: T, toByteOffset offset: Int = 0, as type: T.Type) where T : BitwiseCopyable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablerawspan/storebytes(of:tobyteoffset:as:))*