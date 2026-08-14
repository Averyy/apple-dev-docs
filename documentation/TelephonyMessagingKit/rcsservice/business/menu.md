# RCSService.Business.Menu

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A menu provided by business.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct Menu
```

## Topics

### Accessing menu properties
- [let title: String?](rcsservice/business/menu/title.md)
  Title for menu.
- [let contents: [RCSService.Business.Menu.Content]](rcsservice/business/menu/contents.md)
  Array of menu contents.
- [RCSService.Business.Menu.Content](rcsservice/business/menu/content.md)
  Enumeration defining the contents of menu.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var themeColor: CGColor?](rcsservice/business/themecolor.md)
  Theme color to apply to conversation view.
- [let backgroundImageURL: URL?](rcsservice/business/backgroundimageurl.md)
  Background image to apply to business information page.
- [let styleSheetTemplateURL: URL?](rcsservice/business/stylesheettemplateurl.md)
  URL referring to a CSS template to be used in rich cards sent by business.
- [let persistentMenu: RCSService.Business.Menu?](rcsservice/business/persistentmenu.md)
  Persistent menu with a nested collection of suggested replies and suggested actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/menu)*