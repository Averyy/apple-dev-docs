# version

**Framework**: Core Graphics  
**Kind**: property

The version of this structure. It should be set to 0.

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
var version: UInt32
```

## See Also

- [var getBytePointer: CGDataProviderGetBytePointerCallback?](cgdataproviderdirectcallbacks/getbytepointer.md)
  A pointer to a function that returns a pointer to the provider’s data. For more information, see [`CGDataProviderGetBytePointerCallback`](cgdataprovidergetbytepointercallback.md).
- [var getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback?](cgdataproviderdirectcallbacks/getbytesatposition.md)
  A pointer to a function that copies data from the provider.
- [var releaseBytePointer: CGDataProviderReleaseBytePointerCallback?](cgdataproviderdirectcallbacks/releasebytepointer.md)
  A pointer to a function that Core Graphics calls to release a pointer to the provider’s data. For more information, see [`CGDataProviderReleaseBytePointerCallback`](cgdataproviderreleasebytepointercallback.md).
- [var releaseInfo: CGDataProviderReleaseInfoCallback?](cgdataproviderdirectcallbacks/releaseinfo.md)
  A pointer to a function that handles clean-up for the data provider, or `NULL`. For more information, see [`CGDataProviderReleaseInfoCallback`](cgdataproviderreleaseinfocallback.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataproviderdirectcallbacks/version)*