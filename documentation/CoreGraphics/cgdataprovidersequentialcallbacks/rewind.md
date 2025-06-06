# rewind

**Framework**: Core Graphics  
**Kind**: property

A pointer to a function Core Graphics calls to return the provider to the beginning of the data stream. For more information, see [`CGDataProviderRewindCallback`](cgdataproviderrewindcallback.md).

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
var rewind: CGDataProviderRewindCallback?
```

## See Also

- [var getBytes: CGDataProviderGetBytesCallback?](cgdataprovidersequentialcallbacks/getbytes.md)
  A pointer to a function that copies data from the provider. For more information, see [`CGDataProviderGetBytesCallback`](cgdataprovidergetbytescallback.md).
- [var releaseInfo: CGDataProviderReleaseInfoCallback?](cgdataprovidersequentialcallbacks/releaseinfo.md)
  A pointer to a function that handles clean-up for the data provider, or `NULL`. For more information, see [`CGDataProviderReleaseInfoCallback`](cgdataproviderreleaseinfocallback.md).
- [var skipForward: CGDataProviderSkipForwardCallback?](cgdataprovidersequentialcallbacks/skipforward.md)
  A pointer to a function that Core Graphics calls to advance the stream of data supplied by the provider.
- [var version: UInt32](cgdataprovidersequentialcallbacks/version.md)
  The version of this structure. It should be set to 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataprovidersequentialcallbacks/rewind)*