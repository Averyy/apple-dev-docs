# init(object:owned:)

**Framework**: Apple Archive  
**Kind**: init

Returns a new archive byte stream from the specified traits and entry message processing callback.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
override init(object aaObject: _AAOptionalObjectWrapper<_AAByteStreamTraits>.AAType?, owned aaObjectOwned: Bool)
```

## Parameters

- `aaObject`: An object wrapper that contains the blob traits.
- `aaObjectOwned`: A Boolean value that specifies whether the archive stream owns the traits object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream/init(object:owned:))*