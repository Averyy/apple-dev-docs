# rewind

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

A pointer to a function Core Graphics calls to return the provider to the beginning of the data stream. For more information, see [`CGDataProviderRewindCallback`](../cgdataproviderrewindcallback.md).

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var rewind: CGDataProviderRewindCallback?
```

```c
CGDataProviderRewindCallback rewind;
```

## See Also

### Instance Properties
- [var getBytes: CGDataProviderGetBytesCallback?](./getbytes.md)
  A pointer to a function that copies data from the provider. For more information, see [`CGDataProviderGetBytesCallback`](../cgdataprovidergetbytescallback.md).
- [var releaseInfo: CGDataProviderReleaseInfoCallback?](./releaseinfo.md)
  A pointer to a function that handles clean-up for the data provider, or `NULL`. For more information, see [`CGDataProviderReleaseInfoCallback`](../cgdataproviderreleaseinfocallback.md).
- [var skipForward: CGDataProviderSkipForwardCallback?](./skipforward.md)
  A pointer to a function that Core Graphics calls to advance the stream of data supplied by the provider.
- [var version: UInt32](./version.md)
  The version of this structure. It should be set to 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataprovidersequentialcallbacks/rewind)*