# WKNotificationScene

**Framework**: SwiftUI  
**Kind**: struct

A scene which appears in response to receiving the specified category of remote or local notifications.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
struct WKNotificationScene<Content, Controller> where Content : View, Controller : WKUserNotificationHostingController<Content>
```

## Mentions

- [Declaring a custom view](declaring-a-custom-view.md)

## Topics

### Creating a notification scene
- [init(controller: Controller.Type, category: String)](wknotificationscene/init(controller:category:).md)
  Creates a scene that appears in response to receiving a specific category of remote or local notifications.

## Relationships

### Conforms To
- [Scene](scene.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wknotificationscene)*