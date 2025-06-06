# init(bundleIdentifier:)

**Framework**: Automatic Assessment Configuration  
**Kind**: init

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

#### Discussion

You can get the bundle identifier for an app using the `codesign` command line utility:

```shell
% codesign -v -d /Applications/MyApp.app
```

However, it’s typically more secure to specify both the bundle and team identifiers when creating an app representation using [`init(bundleIdentifier:teamIdentifier:)`](aeassessmentapplication/init(bundleidentifier:teamidentifier:).md).

## Parameters

- `bundleIdentifier`: The bundle identifier of the app.

## See Also

- [init(bundleIdentifier: String, teamIdentifier: String?)](aeassessmentapplication/init(bundleidentifier:teamidentifier:).md)
  Creates a representation of an app using its bundle and team identifiers.
- [var bundleIdentifier: String](aeassessmentapplication/bundleidentifier.md)
  The bundle identifier of the app.
- [var teamIdentifier: String?](aeassessmentapplication/teamidentifier.md)
  The team identifier of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentapplication/init(bundleidentifier:))*