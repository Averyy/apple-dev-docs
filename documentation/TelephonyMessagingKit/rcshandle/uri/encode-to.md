# encode(to:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Encodes this value into the given encoder, when the type’s `RawValue` is `String`.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
func encode(to encoder: any Encoder) throws
```

#### Discussion

This function throws an error if any values are invalid for the given encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcshandle/uri/encode(to:))*