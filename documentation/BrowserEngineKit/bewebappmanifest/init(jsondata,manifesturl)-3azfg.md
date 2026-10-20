# init(jsonData:manifestURL:)

**Framework**: BrowserEngineKit  
**Kind**: init  
**Role**: Initializer

Returns nil if manifestURL is invalid or jsonData cannot be parsed.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- macOS
- tvOS 17.5+
- visionOS 1.2+
- watchOS 10.5+

## Declaration

```swift
init?(jsonData: Data, manifestURL: URL)
```

```objc
- (BEWebAppManifest *) initWithJSONData:(NSData *) jsonData manifestURL:(NSURL *) manifestURL;
```

## See Also

### Creating a web app manifest
- [init?(JSONData: Data, manifestURL: URL)](./init%28jsondata,manifesturl%29-4zjpz.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebappmanifest/init(jsondata:manifesturl:)-3azfg)*