# ExtensionConfigTag

**Framework**: SiriKit Cloud Media  
**Kind**: typealias

A unique identifier for a specific media service configuration.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
string ExtensionConfigTag
```

#### Discussion

Change this value whenever anything in your service’s [`ExtensionConfig`](extensionconfig.md) changes. Don’t include any personally identifiable information in this value and ensure the value matches the `/["][ -~]{1000}["]/` pattern.

## See Also

- [Configure Your Service Endpoints](configuration-resource.md)
  Provide configuration details for your media server’s endpoints to a HomePod speaker or an Apple TV.
- [object ExtensionConfig](extensionconfig.md)
  Instructions for accessing your media service’s endpoints.
- [object PlayMediaControlActivity](playmediacontrolactivity.md)
  Options for reporting playback progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/extensionconfigtag)*