# url

**Framework**: ARKit  
**Kind**: property

The URL encoded in an App Clip Code.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+
- Mac Catalyst 14.3+

## Declaration

```swift
var url: URL? { get }
```

#### Discussion

To enable users to decode your App Clip code’s URL from an App Clip or within an AR app, associate your App Clip with its App Clip Code(s) in App Store Connect; for more information, see [`set up an App Clip experience`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev5b665db74). Because each App Clip Code belongs to a specific App Clip experience, you can decode an App Clip Code URL in a full app’s AR experience only after first providing an accompanying App Clip.

This property is `nil` by default. The framework sets a value for this property when [`urlDecodingState`](arappclipcodeanchor/urldecodingstate-swift.property.md) is [`ARAppClipCodeAnchor.URLDecodingState.decoded`](arappclipcodeanchor/urldecodingstate-swift.enum/decoded.md). This property remains `nil` for App Clip Codes that belong to another App Clip experience or development team.

##### Distribute Your App and App Clip for Testing

Although you can launch an App Clip from the camera after creating an App Clip local experience, ARKit checks the App Clip experience registry in App Store Connect to determine if your App Clip associates to a particular App Clip Code URL. When ARKit confirms that an App Clip Code in the physical environment belongs to your App Clip experience, the framework sets the value of this property.

After setting up an App Clip experience, distribute your app to testers; for more information, see [`Testing the launch experience of your App Clip`](https://developer.apple.com/documentation/AppClip/testing-the-launch-experience-of-your-app-clip).

## See Also

- [var urlDecodingState: ARAppClipCodeAnchor.URLDecodingState](arappclipcodeanchor/urldecodingstate-swift.property.md)
  A state that indicates the process of decoding an App Clip Code URL.
- [ARAppClipCodeAnchor.URLDecodingState](arappclipcodeanchor/urldecodingstate-swift.enum.md)
  The states in the process of decoding an App Clip code URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arappclipcodeanchor/url)*