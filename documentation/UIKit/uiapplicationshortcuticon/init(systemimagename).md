# init(systemImageName:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a Home Screen quick action icon using a system symbol image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
convenience init(systemImageName: String)
```

```objc
+ (instancetype) iconWithSystemImageName:(NSString *) systemImageName;
```

#### Return Value

A Home Screen quick action icon initialized with the specified system symbol image.

## Parameters

- `systemImageName`: The name of the system symbol image. Use the SF Symbols app to look up the names of system symbol images. You can download this app from the design resources page at [developer.apple.com](https://developer.apple.com/design/resources/).

## See Also

### Creating a quick action icon
- [convenience init(type: UIApplicationShortcutIcon.IconType)](./init%28type%29.md)
  Creates a Home Screen quick action icon using a system-defined image.
- [convenience init(templateImageName: String)](./init%28templateimagename%29.md)
  Creates a Home Screen quick action icon based on an image in your app’s bundle, preferably in an asset catalog.
- [convenience init(contact: CNContact)](./init%28contact%29.md)
  Creates a Home Screen quick action icon from the picture for a contact or a monogram of the contact name if the picture is unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/init(systemimagename:))*