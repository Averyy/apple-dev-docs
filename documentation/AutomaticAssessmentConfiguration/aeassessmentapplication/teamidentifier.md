# teamIdentifier

**Framework**: Automatic Assessment Configuration  
**Kind**: property

The team identifier of the app.

**Availability**:
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var teamIdentifier: String? { get }
```

#### Discussion

You can get the team identifier for an app using the `codesign` command line utility:

```shell
% codesign -v -d /Applications/MyApp.app
```

## See Also

- [init(bundleIdentifier: String, teamIdentifier: String?)](aeassessmentapplication/init(bundleidentifier:teamidentifier:).md)
  Creates a representation of an app using its bundle and team identifiers.
- [init(bundleIdentifier: String)](aeassessmentapplication/init(bundleidentifier:).md)
  Creates a representation of an app using its bundle identifier.
- [var bundleIdentifier: String](aeassessmentapplication/bundleidentifier.md)
  The bundle identifier of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentapplication/teamidentifier)*