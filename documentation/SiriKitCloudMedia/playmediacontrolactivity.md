# PlayMediaControlActivity

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

Options for reporting playback progress.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object PlayMediaControlActivity
```

#### Discussion

Provide these values in a [`Queue`](queue.md) to configure when the client sends requests to your [`Report Playback Progress and Activity`](updateactivity.md) endpoint.

If you specify both `playElapsedInterval` and `playElapsed`, the client sends the first report after it plays `playElapsed` seconds of content. Then it sends additional reports according to the `playElapsedInterval`, counting from the beginning of the content. For example, if you specify `45` for `playElapsed` and `30` for `playElapsedInterval`, the client sends reports after 45, 60, 90, and 120 seconds of playback.

If you specify `playElapsedInterval`, but not `playElapsed`, the client uses the `playElapsedInterval` for both.

## See Also

- [Configure Your Service Endpoints](configuration-resource.md)
  Provide configuration details for your media server’s endpoints to a HomePod speaker or an Apple TV.
- [type ExtensionConfigTag](extensionconfigtag.md)
  A unique identifier for a specific media service configuration.
- [object ExtensionConfig](extensionconfig.md)
  Instructions for accessing your media service’s endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playmediacontrolactivity)*