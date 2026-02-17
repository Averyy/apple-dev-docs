# shared

**Framework**: CarPlay  
**Kind**: property

The Now Playing template the system provides.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class var shared: CPNowPlayingTemplate { get }
```

#### Discussion

You do not create instances of `CPNowPlayingTemplate` directly. Instead, use this property to access the shared Now Playing template that CarPlay provides, and then configure its properties accordingly.

You must present this shared instance when your app needs to display Now Playing information. For example, in response to the user tapping a playable item. When CarPlay displays Now Playing information for your app, it presents this shared instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/shared)*