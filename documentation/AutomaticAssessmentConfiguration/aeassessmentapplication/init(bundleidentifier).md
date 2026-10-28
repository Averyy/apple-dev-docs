# init(bundleIdentifier:)

**Framework**: Automatic Assessment Configuration  
**Kind**: init  
**Role**: Initializer

Creates a representation of an app using its bundle identifier.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
init(bundleIdentifier: String)
```

```objc
- (instancetype) initWithBundleIdentifier:(NSString *) bundleIdentifier;
```

## Discussion

You can get the bundle identifier for an app using the `codesign` command line utility:

```shell
% codesign -v -d /Applications/MyApp.app
```

However, it’s typically more secure to specify both the bundle and team identifiers when creating an app representation using [`init(bundleIdentifier:teamIdentifier:)`](./init%28bundleidentifier,teamidentifier%29.md).

## Parameters

- `bundleIdentifier`: The bundle identifier of the app.

## See Also

### Creating an assessment application
- [init(bundleIdentifier: String, teamIdentifier: String?)](./init%28bundleidentifier,teamidentifier%29.md)
  Creates a representation of an app using its bundle and team identifiers.
- [var bundleIdentifier: String](./bundleidentifier.md)
  The bundle identifier of the app.
- [var teamIdentifier: String?](./teamidentifier.md)
  The team identifier of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentapplication/init(bundleidentifier:))*