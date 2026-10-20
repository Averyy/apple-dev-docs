# isDataCacheInhibited

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that instructs FSKit not to call this protocol’s methods, even if the volume conforms to it.

**Availability**:
- macOS 27.0+

## Declaration

```swift
optional var isDataCacheInhibited: Bool { get }
```

```objc
@property (readonly, getter=isDataCacheInhibited) BOOL dataCacheInhibited;
```

#### Discussion

FSKit reads this value after the file system replies to the `loadResource` message. Changing the returned value during the runtime of the volume has no effect.

> **Note**: This property does not disable data caching; it only disables the usage of the protocol. In order to completely disable data caching, return the [`FSVolume.KernelCacheCoherencyType.noCache`](../kernelcachecoherencytype/nocache.md) coherency type from [`open(_:modes:cacheMode:context:replyHandler:)`](./open%28_,modes,cachemode,context,replyhandler%29.md) for all items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/datacachehandler/isdatacacheinhibited)*