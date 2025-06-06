# releaseBytePointer

**Framework**: Core Graphics  
**Kind**: property

A pointer to a function that Core Graphics calls to release a pointer to the provider’s data. For more information, see [`CGDataProviderReleaseBytePointerCallback`](cgdataproviderreleasebytepointercallback.md).

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var releaseBytePointer: CGDataProviderReleaseBytePointerCallback?
```

## See Also

- [var getBytePointer: CGDataProviderGetBytePointerCallback?](cgdataproviderdirectcallbacks/getbytepointer.md)
  A pointer to a function that returns a pointer to the provider’s data. For more information, see [`CGDataProviderGetBytePointerCallback`](cgdataprovidergetbytepointercallback.md).
- [var getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback?](cgdataproviderdirectcallbacks/getbytesatposition.md)
  A pointer to a function that copies data from the provider.
- [var releaseInfo: CGDataProviderReleaseInfoCallback?](cgdataproviderdirectcallbacks/releaseinfo.md)
  A pointer to a function that handles clean-up for the data provider, or `NULL`. For more information, see [`CGDataProviderReleaseInfoCallback`](cgdataproviderreleaseinfocallback.md).
- [var version: UInt32](cgdataproviderdirectcallbacks/version.md)
  The version of this structure. It should be set to 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataproviderdirectcallbacks/releasebytepointer)*