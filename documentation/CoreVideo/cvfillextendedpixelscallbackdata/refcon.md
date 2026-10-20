# refCon

**Framework**: Core Video  
**Kind**: property  
**Role**: Instance Property

A pointer to application-defined data that is passed to your custom pixel fill function.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var refCon: UnsafeMutableRawPointer?
```

```c
void * refCon;
```

## See Also

### Properties
- [var fillCallBack: CVFillExtendedPixelsCallBack?](./fillcallback.md)
- [var version: CFIndex](./version.md)
  The version of this fill algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvfillextendedpixelscallbackdata/refcon)*