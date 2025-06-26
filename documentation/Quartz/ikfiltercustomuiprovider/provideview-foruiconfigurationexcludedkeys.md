# provideView(forUIConfiguration:excludedKeys:)

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Provides a custom view for a filter.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func provideView(forUIConfiguration inUIConfiguration: [AnyHashable : Any]!, excludedKeys inKeys: [Any]!) -> IKFilterUIView!
```

#### Return Value

An [`IKFilterUIView`](ikfilteruiview.md) object or `nil` if the filter is unable to provide a view. If `nil`, the Image Kit framework will attempt to provide a user interface.

#### Discussion

This method overrides the method [`view(forUIConfiguration:excludedKeys:)`](https://developer.apple.com/documentation/CoreImage/CIFilter-swift.class/view(forUIConfiguration:excludedKeys:)).

## Parameters

- `inUIConfiguration`: A dictionary that specifies the size of the controls.  Provide the key   and one of the following values:  ,  , or   . For more information on these constants, see   in CIFilter Image Kit Additions.
- `inKeys`: An array of the input keys for which you do   want to provide a user interface. Pass   if you want all input keys to be represented in the user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikfiltercustomuiprovider/provideview(foruiconfiguration:excludedkeys:))*