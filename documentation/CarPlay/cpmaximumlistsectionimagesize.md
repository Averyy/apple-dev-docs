# CPMaximumListSectionImageSize

**Framework**: CarPlay  
**Kind**: var  
**Role**: Global Variable

The maximum size of images you include in section headers.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+

## Declaration

```swift
let CPMaximumListSectionImageSize: CGSize
```

```c
extern const CGSize CPMaximumListSectionImageSize;
```

## Discussion

This value is in points. To get the image dimensions in pixels, multiple the size values by the scale factor in the [`carTraitCollection`](./cpinterfacecontroller/cartraitcollection.md) property of your interface controller.

## See Also

### Creating a section
- [convenience init(items: [any CPListTemplateItem])](./cplistsection/init%28items%29-6ksy3.md)
- [convenience init(items: [any CPListTemplateItem], header: String?, sectionIndexTitle: String?)](./cplistsection/init%28items,header,sectionindextitle%29-6xewg.md)
- [init(items: [any CPListTemplateItem], header: String, headerSubtitle: String?, headerImage: UIImage?, headerButton: CPButton?, sectionIndexTitle: String?)](./cplistsection/init%28items,header,headersubtitle,headerimage,headerbutton,sectionindextitle%29.md)
  Creates a section with list items, a header, a section index title, and section header details.
- [convenience init(items: [CPListItem])](./cplistsection/init%28items%29-32d0q.md)
- [convenience init(items: [CPListItem], header: String?, sectionIndexTitle: String?)](./cplistsection/init%28items,header,sectionindextitle%29-743we.md)
- [init?(coder: NSCoder)](./cplistsection/init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaximumlistsectionimagesize)*