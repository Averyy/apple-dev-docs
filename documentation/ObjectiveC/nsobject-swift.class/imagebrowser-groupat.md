# imageBrowser(_:groupAt:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns the group at the specified index.

**Availability**:
- macOS ?+

## Declaration

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, groupAt index: Int) -> [AnyHashable : Any]!
```

#### Return Value

A dictionary that defines the group. The keys in this dictionary can be any of the following constants: [`IKImageBrowserGroupStyleKey`](https://developer.apple.com/documentation/quartz/ikimagebrowsergroupstylekey), [`IKImageBrowserGroupBackgroundColorKey`](https://developer.apple.com/documentation/quartz/ikimagebrowsergroupbackgroundcolorkey), [`IKImageBrowserGroupTitleKey`](https://developer.apple.com/documentation/quartz/ikimagebrowsergrouptitlekey), and [`IKImageBrowserGroupRangeKey`](https://developer.apple.com/documentation/quartz/ikimagebrowsergrouprangekey). For more information on these constants, see [`IKImageBrowserView`](https://developer.apple.com/documentation/quartz/ikimagebrowserview).

#### Discussion

This method is optional.

## Parameters

- `aBrowser`: An image browser view.
- `index`: The index of the group you want to retrieve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:groupat:))*