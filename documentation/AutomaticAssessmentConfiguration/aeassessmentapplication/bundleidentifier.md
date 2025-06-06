# bundleIdentifier

**Framework**: Automatic Assessment Configuration  
**Kind**: property

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

#### Discussion

You can get the bundle identifier for an app using the `codesign` command line utility:

```shell
% codesign -v -d /Applications/MyApp.app
```

## See Also

- [init(bundleIdentifier: String, teamIdentifier: String?)](aeassessmentapplication/init(bundleidentifier:teamidentifier:).md)
  Creates a representation of an app using its bundle and team identifiers.
- [init(bundleIdentifier: String)](aeassessmentapplication/init(bundleidentifier:).md)
  Creates a representation of an app using its bundle identifier.
- [var teamIdentifier: String?](aeassessmentapplication/teamidentifier.md)
  The team identifier of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentapplication/bundleidentifier)*