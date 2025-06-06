# persistableContentKey(fromKeyVendorResponse:options:)

**Framework**: AVFoundation  
**Kind**: method

Creates a persistable content key from the content key context data.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func persistableContentKey(fromKeyVendorResponse keyVendorResponse: Data, options: [String : Any]? = nil) throws -> Data
```

#### Return Value

Returns a data object that contains the persistable content key.

## Parameters

- `keyVendorResponse`: The response returned from the key vendor.
- `options`: Additional information required to obtain the persistable content key. The value of this parameter is   when no additional information is required.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpersistablecontentkeyrequest/persistablecontentkey(fromkeyvendorresponse:options:))*