# webPlugInContainerLoad(_:inFrame:)

**Framework**: Objective-C Runtime  
**Kind**: method

Loads a URL into a web frame.

**Availability**:
- macOS ?+

## Declaration

```swift
func webPlugInContainerLoad(_ request: URLRequest!, inFrame target: String!)
```

#### Discussion

If the frame specified by `target` is not found, a new window is opened, loaded with the URL request, and given the specified frame name. If `target` is `nil`, the frame enclosing the plug-in is loaded with the URL request.

## Parameters

- `request`: The request that specifies the URL.
- `target`: The frame into which the URL is loaded.

## See Also

- [func webPlugInContainerShowStatus(String!)](nsobject-swift.class/webplugincontainershowstatus(_:).md)
  Tells the container to show a status message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webplugincontainerload(_:inframe:))*