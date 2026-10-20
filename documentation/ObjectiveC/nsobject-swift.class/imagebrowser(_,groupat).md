# imageBrowser(_:groupAt:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns the group at the specified index.

**Availability**:
- macOS

## Declaration

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, groupAt index: Int) -> [AnyHashable : Any]!
```

```objc
- (NSDictionary *) imageBrowser:(IKImageBrowserView *) aBrowser groupAtIndex:(NSUInteger) index;
```

#### Return Value

A dictionary that defines the group. The keys in this dictionary can be any of the following constants: [`IKImageBrowserGroupStyleKey`](../../Quartz/ikimagebrowsergroupstylekey.md), [`IKImageBrowserGroupBackgroundColorKey`](../../Quartz/ikimagebrowsergroupbackgroundcolorkey.md), [`IKImageBrowserGroupTitleKey`](../../Quartz/ikimagebrowsergrouptitlekey.md), and [`IKImageBrowserGroupRangeKey`](../../Quartz/ikimagebrowsergrouprangekey.md). For more information on these constants, see [`IKImageBrowserView`](../../Quartz/ikimagebrowserview.md).

#### Discussion

This method is optional.

## Parameters

- `aBrowser`: An image browser view.
- `index`: The index of the group you want to retrieve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:groupat:))*