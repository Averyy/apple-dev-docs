# init(bundleIdentifier:teamIdentifier:)

**Framework**: Automatic Assessment Configuration  
**Kind**: init  
**Role**: Initializer

Creates a representation of an app using its bundle and team identifiers.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
init(bundleIdentifier: String, teamIdentifier: String?)
```

```objc
- (instancetype) initWithBundleIdentifier:(NSString *) bundleIdentifier teamIdentifier:(NSString *) teamIdentifier;
```

#### Discussion

You can get the bundle and team identifiers for an app using the `codesign` command line utility:

```shell
% codesign -v -d /Applications/MyApp.app
```

## Parameters

- `bundleIdentifier`: The bundle identifier of the app.
- `teamIdentifier`: The team identifier of the team that distributes the app.

## See Also

### Creating an assessment application
- [init(bundleIdentifier: String)](./init%28bundleidentifier%29.md)
  Creates a representation of an app using its bundle identifier.
- [var bundleIdentifier: String](./bundleidentifier.md)
  The bundle identifier of the app.
- [var teamIdentifier: String?](./teamidentifier.md)
  The team identifier of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentapplication/init(bundleidentifier:teamidentifier:))*