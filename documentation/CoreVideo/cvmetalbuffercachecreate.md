# CVMetalBufferCacheCreate(_:_:_:_:)

**Framework**: Core Video  
**Kind**: func

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func CVMetalBufferCacheCreate(_ allocator: CFAllocator?, _ cacheAttributes: CFDictionary?, _ metalDevice: any MTLDevice, _ cacheOut: UnsafeMutablePointer<CVMetalBufferCache?>) -> CVReturn
```

#### Return Value

Returns kCVReturnSuccess on success

#### Discussion

Creates a new Buffer Cache.

## Parameters

- `allocator`: The CFAllocatorRef to use for allocating the cache.  May be NULL.
- `cacheAttributes`: A CFDictionaryRef containing the attributes of the cache itself. May be NULL.
- `metalDevice`: The Metal device for which the buffer objects will be created.
- `cacheOut`: The newly created buffer cache will be placed here


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetalbuffercachecreate(_:_:_:_:))*