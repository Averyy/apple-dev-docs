# provideView(forUIConfiguration:excludedKeys:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides a custom view for a filter.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func provideView(forUIConfiguration inUIConfiguration: [AnyHashable : Any]!, excludedKeys inKeys: [Any]!) -> IKFilterUIView!
```

```objc
- (IKFilterUIView *) provideViewForUIConfiguration:(NSDictionary *) inUIConfiguration excludedKeys:(NSArray *) inKeys;
```

## Return Value

An [`IKFilterUIView`](../ikfilteruiview.md) object or `nil` if the filter is unable to provide a view. If `nil`, the Image Kit framework will attempt to provide a user interface.

## Discussion

This method overrides the method [`view(forUIConfiguration:excludedKeys:)`](../../CoreImage/cifilter-swift.class/view%28foruiconfiguration,excludedkeys%29.md).

## Parameters

- `inUIConfiguration`: A dictionary that specifies the size of the controls.  Provide the key `IKUISizeFlavor` and one of the following values: `IKUISizeMini`, `IKUISizeSmall`, or  `IKUISizeRegular`. For more information on these constants, see *User Interface Options* in CIFilter Image Kit Additions.
- `inKeys`: An array of the input keys for which you do *not* want to provide a user interface. Pass `nil` if you want all input keys to be represented in the user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikfiltercustomuiprovider/provideview(foruiconfiguration:excludedkeys:))*