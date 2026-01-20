# filter(withName:)

**Framework**: Core Image  
**Kind**: method  
**Required**: Yes

Returns a filter object specified by name.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func filter(withName name: String) -> CIFilter?
```

#### Return Value

A [`CIFilter`](cifilter-swift.class.md) object implementing the custom filter.

#### Discussion

Core Image calls this method when a filter is requested by name using the [`CIFilter`](cifilter-swift.class.md) class method [`init(name:)`](cifilter-swift.class/init(name:).md) method (or related methods). Your implementation of this method should provide a new instance of the [`CIFilter`](cifilter-swift.class.md) subclass for your custom filter.

## Parameters

- `name`: The name of the requested custom filter.

## See Also

- [Core Image Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilterconstructor/filter(withname:))*