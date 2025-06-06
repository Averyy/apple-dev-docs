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

A dictionary that defines the group. The keys in this dictionary can be any of the following constants: [`IKImageBrowserGroupStyleKey`](https://developer.apple.com/documentation/Quartz/IKImageBrowserGroupStyleKey), [`IKImageBrowserGroupBackgroundColorKey`](https://developer.apple.com/documentation/Quartz/IKImageBrowserGroupBackgroundColorKey), [`IKImageBrowserGroupTitleKey`](https://developer.apple.com/documentation/Quartz/IKImageBrowserGroupTitleKey), and [`IKImageBrowserGroupRangeKey`](https://developer.apple.com/documentation/Quartz/IKImageBrowserGroupRangeKey). For more information on these constants, see [`IKImageBrowserView`](https://developer.apple.com/documentation/Quartz/IKImageBrowserView).

#### Discussion

This method is optional.

## Parameters

- `aBrowser`: An image browser view.
- `index`: The index of the group you want to retrieve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:groupat:))*