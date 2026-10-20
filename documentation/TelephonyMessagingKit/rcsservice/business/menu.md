# RCSService.Business.Menu

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A menu provided by business.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct Menu
```

## Topics

### Accessing menu properties
- [let title: String?](./menu/title.md)
  Title for menu.
- [let contents: [RCSService.Business.Menu.Content]](./menu/contents.md)
  Array of menu contents.
- [RCSService.Business.Menu.Content](./menu/content.md)
  Enumeration defining the contents of menu.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Accessing display information
- [var themeColor: CGColor?](./themecolor.md)
  Theme color to apply to conversation view.
- [let backgroundImageURL: URL?](./backgroundimageurl.md)
  Background image to apply to business information page.
- [let styleSheetTemplateURL: URL?](./stylesheettemplateurl.md)
  URL referring to a CSS template to be used in rich cards sent by business.
- [let persistentMenu: RCSService.Business.Menu?](./persistentmenu.md)
  Persistent menu with a nested collection of suggested replies and suggested actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/menu)*