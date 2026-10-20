# onOpenURL(perform:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Registers a handler to invoke in response to a URL that your app receives.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func onOpenURL(perform action: @escaping (URL) -> ()) -> some View
```

#### Return Value

A view that handles incoming URLs.

#### Discussion

Use this view modifier to receive URLs in a particular scene within your app. The scene that SwiftUI routes the incoming URL to depends on the structure of your app, what scenes are active, and other configuration. For more information, see [`handlesExternalEvents(matching:)`](../scene/handlesexternalevents%28matching%29.md).

UI frameworks traditionally pass Universal Links to your app using an [`NSUserActivity`](../../Foundation/nsuseractivity.md). However, SwiftUI passes a Universal Link to your app directly as a URL, which you receive using this modifier. To receive other user activities, like when your app participates in Handoff, use the [`onContinueUserActivity(_:perform:)`](./oncontinueuseractivity%28_,perform%29.md) modifier instead.

For more information about linking into your app, see [Allowing apps and websites to link to your content](../../Xcode/allowing-apps-and-websites-to-link-to-your-content.md).

## Parameters

- `action`: A closure that SwiftUI calls when your app receives a Universal Link or a custom [`URL`](../../Foundation/url.md). The closure takes the URL as an input parameter.

## See Also

### Sending and receiving URLs
- [var openURL: OpenURLAction](../environmentvalues/openurl.md)
  An action that opens a URL.
- [struct OpenURLAction](../openurlaction.md)
  An action that opens a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onopenurl(perform:))*