# write(to:)

**Framework**: Swift  
**Kind**: method

Writes the string into the given output stream.

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
func write<Target>(to target: inout Target) where Target : TextOutputStream
```

## Parameters

- `target`: An output stream.

## See Also

- [func write(String)](string/write(_:).md)
  Appends the given string to this string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/write(to:))*