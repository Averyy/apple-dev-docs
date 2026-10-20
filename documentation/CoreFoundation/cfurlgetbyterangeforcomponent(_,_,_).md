# CFURLGetByteRangeForComponent(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the range of the specified component in the bytes of a URL.

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
func CFURLGetByteRangeForComponent(_ url: CFURL!, _ component: CFURLComponentType, _ rangeIncludingSeparators: UnsafeMutablePointer<CFRange>!) -> CFRange
```

```c
extern CFRange CFURLGetByteRangeForComponent(CFURLRef url, CFURLComponentType component, CFRange *rangeIncludingSeparators);
```

#### Return Value

The range of bytes for `component` in the buffer returned by the [`CFURLGetBytes(_:_:_:)`](./cfurlgetbytes%28_,_,_%29.md) function. If `anURL` does not contain `component`, the first part of the returned range is set to [`kCFNotFound`](./kcfnotfound.md).

#### Discussion

This function is intended to be used in conjunction with the [`CFURLGetBytes(_:_:_:)`](./cfurlgetbytes%28_,_,_%29.md) function, since the range returned is only applicable to the bytes returned by [`CFURLGetBytes(_:_:_:)`](./cfurlgetbytes%28_,_,_%29.md).

## Parameters

- `url`: The URL containing `component`.
- `component`: The type of component in `anURL` whose range you want to obtain. See [`CFURLComponentType`](./cfurlcomponenttype.md) for possible values.
- `rangeIncludingSeparators`: Specifies the range of `component` including the sequences that separate component from the previous and next components. If there is no previous or next components, this function will match the range of the component itself. If `anURL` does not contain `component`, `rangeIncludingSeparators` is set to the location where the component would be inserted.

## See Also

### Getting URL Properties
- [func CFURLGetBaseURL(CFURL!) -> CFURL!](./cfurlgetbaseurl%28_%29.md)
  Returns the base URL of a given URL if it exists.
- [func CFURLGetBytes(CFURL!, UnsafeMutablePointer<UInt8>!, CFIndex) -> CFIndex](./cfurlgetbytes%28_,_,_%29.md)
  Returns by reference the byte representation of a URL object.
- [func CFURLGetTypeID() -> CFTypeID](./cfurlgettypeid%28%29.md)
  Returns the type identifier for the `CFURL` opaque type.
- [func CFURLResourceIsReachable(CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./cfurlresourceisreachable%28_,_%29.md)
  Returns whether the resource pointed to by a file URL can be reached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlgetbyterangeforcomponent(_:_:_:))*