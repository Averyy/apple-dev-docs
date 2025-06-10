# open(_:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Asks the system to open a URL on behalf of the currently running app extension.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func open(_ URL: URL) async -> Bool
```

#### Discussion

Each extension point determines whether to support this method, or under which conditions to support this method. In iOS,  the Today and iMessage app extension points support this method. An iMessage app extension can use this method only to open its parent app, and only if the parent app is shown on the iOS home screen.

> ❗ **Important**:  You can use this method in a Today widget to open the widget’s containing app. If you use this method to open other apps from your Today widget, your App Store submission may require additional review. To learn more, see [`App Store Review Guidelines`](https://developer.apple.comhttp://developer.apple.com/appstore/resources/approval/guidelines.html) and [`iOS Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/ios/human-interface-guidelines/).

## Parameters

- `URL`: The URL to open.
- `completionHandler`: A block/closure to be called when the URL has opened. The closure takes a single boolean parameter indicating whether the operation was successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensioncontext/open(_:completionhandler:))*