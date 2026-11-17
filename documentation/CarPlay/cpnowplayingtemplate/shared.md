# shared

**Framework**: CarPlay  
**Kind**: property  
**Role**: Type Property

The shared Now Playing template for you to configure and display.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class var shared: CPNowPlayingTemplate { get }
```

```objc
@property (class, nonatomic, strong, readonly) CPNowPlayingTemplate * sharedTemplate;
```

## Discussion

Use this property to access the singleton `CPNowPlayingTemplate` object and configure it. At launch time, configure this instance and register an observer to support features like the Album Artist and Up Next button. While your app is running, you can present the template directly from your interface to reflect the currently playing item. For example, if someone plays an album, you might show this interface so the person can monitor playback and see upcoming tracks. The system can also present your app’s shared Now Playing interface from the Now Playing app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/shared)*