# init(scene:)

**Framework**: BrowserKit  
**Kind**: init  
**Role**: Initializer

Initializes an export manager with your app’s window scene.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
@MainActor
init(scene: UIWindowScene)
```

```objc
- (instancetype) initWithScene:(UIWindowScene *) scene;
```

## Parameters

- `scene`: Your app’s window scene. The manager presents the export sheet in this window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdataexportmanager/init(scene:))*