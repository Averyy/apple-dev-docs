# write(toFile:atomically:encoding:)

**Framework**: Swift  
**Kind**: method

Writes the contents of the `String` to a file at a given path using a given encoding.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func write<T>(toFile path: T, atomically useAuxiliaryFile: Bool, encoding enc: String.Encoding) throws where T : StringProtocol
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/write(tofile:atomically:encoding:))*