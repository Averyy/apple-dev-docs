# init(sourceApplicationBundleIdentifier:sourceApplicationLocalizedName:)

**Framework**: BrowserKit  
**Kind**: init  
**Role**: Initializer

Initializes browser data with the source app’s identifier and display name.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
init(sourceApplicationBundleIdentifier: String?, sourceApplicationLocalizedName: String?)
```

```objc
- (instancetype) initWithSourceApplicationBundleIdentifier:(NSString *) sourceApplicationBundleIdentifier sourceApplicationLocalizedName:(NSString *) sourceApplicationLocalizedName;
```

## Parameters

- `sourceApplicationBundleIdentifier`: The bundle identifier of the source browser app.
- `sourceApplicationLocalizedName`: The localized display name of the source browser app.

## See Also

### Creating a representation of browser data
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Initializes browser data from a decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdata/init(sourceapplicationbundleidentifier:sourceapplicationlocalizedname:))*