---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configbytesfromstringdecoder/decode(_:)"
framework: "swift-configuration/Configuration"
---

# decode(_:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Decodes a string value into an array of bytes.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func decode(_ value: String) -> [UInt8]?
```

## Return Value

An array of bytes if decoding succeeds, or `nil` if it fails.

## Discussion

This method attempts to parse the provided string according to the decoder’s specific format and returns the corresponding byte array. If the string cannot be decoded (due to invalid format or encoding), the method returns `nil`.

## Parameters

- `value`: The string representation to decode.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configbytesfromstringdecoder/decode(_:))*