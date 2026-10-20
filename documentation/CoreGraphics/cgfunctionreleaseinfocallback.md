# CGFunctionReleaseInfoCallback

**Framework**: Core Graphics  
**Kind**: typealias  
**Role**: Type Alias

Performs custom clean-up tasks when Core Graphics deallocates a `CGFunctionRef` object.

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
typealias CGFunctionReleaseInfoCallback = (UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(void *) CGFunctionReleaseInfoCallback;
```

## Parameters

- `info`: The `info` parameter passed to [`init(info:domainDimension:domain:rangeDimension:range:callbacks:)`](./cgfunction/init%28info,domaindimension,domain,rangedimension,range,callbacks%29.md).

## See Also

### Callbacks
- [struct CGFunctionCallbacks](./cgfunctioncallbacks.md)
  A structure that contains callbacks needed by a `CGFunctionRef` object.
- [typealias CGFunctionEvaluateCallback](./cgfunctionevaluatecallback.md)
  Performs custom operations on the supplied input data to produce output data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfunctionreleaseinfocallback)*