# bundleIdentifier

**Framework**: Automatic Assessment Configuration  
**Kind**: property  
**Role**: Instance Property

The bundle identifier of the app.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var bundleIdentifier: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * bundleIdentifier;
```

## Discussion

You can get the bundle identifier for an app using the `codesign` command line utility:

```shell
% codesign -v -d /Applications/MyApp.app
```

## See Also

### Creating an assessment application
- [init(bundleIdentifier: String, teamIdentifier: String?)](./init%28bundleidentifier,teamidentifier%29.md)
  Creates a representation of an app using its bundle and team identifiers.
- [init(bundleIdentifier: String)](./init%28bundleidentifier%29.md)
  Creates a representation of an app using its bundle identifier.
- [var teamIdentifier: String?](./teamidentifier.md)
  The team identifier of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentapplication/bundleidentifier)*